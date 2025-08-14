# FastAPI Stripe Payment API

This project is a simple FastAPI application that allows you to create and view payments using Stripe. It uses the Stripe API in **sandbox mode** for testing purposes.

---

## Features

- **`/pay` POST endpoint**: Creates a payment on Stripe.
- **`/payments` GET endpoint**: Retrieves all payments from Stripe.

- **`/product/create` POST endpoint**: Creates a product on Stripe.
- **`/product/delete/{product_id}` POST endpoint**: Delete a product from Stripe.
- **`/product/modify/{product_id}` POST endpoint**: Modify a profuct from Stripe.
- **`/product/{product_id}` GET endpoint**: Retrieves single product from Stripe.
- **`/products` GET endpoint**: Retrieves all products from Stripe.

- **Stripe Sandbox**: All payments are processed in test mode.
- Easy setup via `.env` file for your Stripe API keys.

---

## Files

- **payments/main.py**: payments main service file.
- **payments/test_payment.py**: This file can make post request to `/payments` endpoint for testing.

- **products/main.py**: products main service file.
- **products/test_products.py**: This file can make post request to `/product/create, /product/delete/{product_id}, /product/modify/{product_id}` endpoint for testing.

---

## Future Plans

- Costumer Charges
- Costumer Subscriptions
- Costumer Invoices
- Costumer Coupons and Promotions
- Costumer Subscription Schedules
- Product Price with Payment Integration
- Payment Intents : 3D Secure
- Payment Refunds
- Payment Tax and Reporting
- Setup Intents : Card and Location
- Sales and Profits based on Product
- Revenue Reports: Daily, Monthly, Yearly
- Subscription Revenue Reports
- Refund and Chargeback Reports
- Webhooks : Real Time Data
