# FastAPI Stripe Payment API

This project is a simple FastAPI application that allows you to create and view payments using Stripe. It uses the Stripe API in **sandbox mode** for testing purposes.

---


## Features

- **`/pay` POST endpoint**: Creates a payment for a specific product on Stripe. You must provide a `product_id` and a payment `source`. The amount and currency are automatically fetched from the product's Stripe price.
- **`/payments` GET endpoint**: Retrieves all payments from Stripe.

- **`/product/create` POST endpoint**: Creates a product on Stripe.
- **`/product/delete/{product_id}` DELETE endpoint**: Delete a product from Stripe.
- **`/product/modify/{product_id}` PUT endpoint**: Modify a product from Stripe.
- **`/product/{product_id}` GET endpoint**: Retrieves single product from Stripe.
- **`/products` GET endpoint**: Retrieves all products from Stripe.

- **Stripe Sandbox**: All payments are processed in test mode.
- Easy setup via `.env` file for your Stripe API keys.

---


## Files

- **payments/main.py**: Payments main service file. Handles payment creation for products.
- **payments/test_payment.py**: Example test file for making a payment for a product (requires a valid product ID).

- **products/main.py**: Products main service file.
- **products/test_products.py**: Example test file for creating, deleting, and modifying products.

---


## Usage

### Payment Example

To make a payment, send a POST request to `/pay` with the following JSON body:

```
{
	"product_id": "<stripe_product_id>",
	"source": "tok_visa"  // or another Stripe test token
}
```

The amount and currency will be automatically determined from the product's price.

---

## Future Plans

- Costumer Charges
- Costumer Subscriptions
- Costumer Invoices
- Costumer Coupons and Promotions
- Costumer Subscription Schedules
- Payment Intents : 3D Secure
- Payment Refunds
- Payment Tax and Reporting
- Setup Intents : Card and Location
- Sales and Profits based on Product
- Revenue Reports: Daily, Monthly, Yearly
- Subscription Revenue Reports
- Refund and Chargeback Reports
- Webhooks : Real Time Data
