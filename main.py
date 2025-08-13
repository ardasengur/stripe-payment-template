
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import stripe
from dotenv import load_dotenv
import os


app = FastAPI()
load_dotenv()
stripe.api_key = os.getenv("stripe_api_key")

class PaymentRequest(BaseModel):
    amount: int 
    currency: str = "try"
    source: str  

@app.post("/pay")
def create_payment(payment: PaymentRequest):
    try:
        charge = stripe.Charge.create(
            amount=payment.amount,
            currency=payment.currency,
            source=payment.source,
            description="Test payment from FastAPI app"
        )
        return {"status": charge["status"], "id": charge["id"]}
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=str(e))


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