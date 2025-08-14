

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import stripe
from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv()
stripe.api_key = os.getenv("stripe_api_key")

class ProductCreate(BaseModel):
    name: str
    description: str = None
    active: bool = True
    metadata: dict = None
    price: float
    currency: str = "usd"
    stock: int = 0

class ProductModify(BaseModel):
    name: str = None
    description: str = None
    active: bool = None
    metadata: dict = None
    price: float = None
    currency: str = None
    stock: int = None

@app.post("/product/create")
def create_product(product: ProductCreate):
    try:
        product_data = product.dict(exclude_none=True)
        price = product_data.pop("price")
        currency = product_data.pop("currency", "usd")
        stock = product_data.pop("stock", 0)
        metadata = product_data.get("metadata", {}) or {}
        metadata["stock"] = str(stock)
        product_data["metadata"] = metadata
        stripe_product = stripe.Product.create(**product_data)
        stripe_price = stripe.Price.create(
            product=stripe_product.id,
            unit_amount=int(price * 100),
            currency=currency
        )
        return {
            "id": stripe_product.id,
            "name": stripe_product.name,
            "description": stripe_product.description,
            "active": stripe_product.active,
            "metadata": stripe_product.metadata,
            "stock": int(stripe_product.metadata.get("stock", 0)),
            "price": stripe_price.unit_amount / 100,
            "currency": stripe_price.currency,
            "price_id": stripe_price.id
        }

    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/product/{product_id}")
def get_product(product_id: str):
    try:
        product = stripe.Product.retrieve(product_id)
        prices = stripe.Price.list(product=product_id, limit=1)
        price_info = None
        if prices.data:
            price_info = {
                "price": prices.data[0].unit_amount / 100,
                "currency": prices.data[0].currency,
                "price_id": prices.data[0].id
            }
        stock = int(product.metadata.get("stock", 0)) if product.metadata and "stock" in product.metadata else 0
        return {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "active": product.active,
            "metadata": product.metadata,
            "stock": stock,
            **(price_info or {})
        }
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/product/delete/{product_id}")
def delete_product(product_id: str):
    try:
        deleted = stripe.Product.delete(product_id)
        return deleted
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/product/modify/{product_id}")
def modify_product(product_id: str, product: ProductModify):
    try:
        product_data = product.dict(exclude_none=True)
        price = product_data.pop("price", None)
        currency = product_data.pop("currency", None)
        stock = product_data.pop("stock", None)
        if stock is not None:
            current_product = stripe.Product.retrieve(product_id)
            metadata = current_product.metadata or {}
            metadata["stock"] = str(stock)
            product_data["metadata"] = metadata
        updated_product = stripe.Product.modify(product_id, **product_data)
        price_info = None
        if price is not None:
            if not currency:
                prices = stripe.Price.list(product=product_id, limit=1)
                if prices.data:
                    currency = prices.data[0].currency
                else:
                    currency = "usd"
            new_price = stripe.Price.create(
                product=product_id,
                unit_amount=int(price * 100),
                currency=currency
            )
            price_info = {
                "price": new_price.unit_amount / 100,
                "currency": new_price.currency,
                "price_id": new_price.id
            }
        else:
            prices = stripe.Price.list(product=product_id, limit=1)
            if prices.data:
                price_info = {
                    "price": prices.data[0].unit_amount / 100,
                    "currency": prices.data[0].currency,
                    "price_id": prices.data[0].id
                }
        return {
            "id": updated_product.id,
            "name": updated_product.name,
            "description": updated_product.description,
            "active": updated_product.active,
            "metadata": updated_product.metadata,
            "stock": int(updated_product.metadata.get("stock", 0)),
            **(price_info or {})
        }
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/products")
def list_products():
    try:
        products = stripe.Product.list()
        product_list = []
        for product in products.data:
            prices = stripe.Price.list(product=product.id, limit=1)
            price_info = None
            if prices.data:
                price_info = {
                    "price": prices.data[0].unit_amount / 100,
                    "currency": prices.data[0].currency,
                    "price_id": prices.data[0].id
                }
            stock = int(product.metadata.get("stock", 0)) if product.metadata and "stock" in product.metadata else 0
            product_list.append({
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "active": product.active,
                "metadata": product.metadata,
                "stock": stock,
                **(price_info or {})
            })
        return {"products": product_list}
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=str(e))