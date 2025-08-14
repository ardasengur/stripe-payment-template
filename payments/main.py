
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import stripe
from dotenv import load_dotenv
import os


app = FastAPI()
load_dotenv()
stripe.api_key = os.getenv("stripe_api_key")


class PaymentRequest(BaseModel):
    product_id: str
    source: str


@app.post("/pay")
def create_payment(payment: PaymentRequest):
    try:
        # Ürün bilgisini Stripe üzerinden al
        product = stripe.Product.retrieve(payment.product_id)
        prices = stripe.Price.list(product=payment.product_id, limit=1)
        if not prices.data:
            raise HTTPException(status_code=404, detail="Product price not found.")
        price = prices.data[0]
        amount = price.unit_amount
        currency = price.currency
        charge = stripe.Charge.create(
            amount=amount,
            currency=currency,
            source=payment.source,
            description=f"Payment for product: {product.name}"
        )
        return {"status": charge["status"], "id": charge["id"], "product_id": payment.product_id}
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/payments")
def list_payments(limit: int = 10):
    try:
        charges = stripe.Charge.list(limit=limit)
        return {"payments": [
            {
                "id": c.id,
                "amount": c.amount,
                "currency": c.currency,
                "status": c.status,
                "created": c.created
            } for c in charges.data
        ]}
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=str(e))