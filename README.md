# FastAPI Stripe Payment API

This project is a simple FastAPI application that allows you to create and view payments using Stripe. It uses the Stripe API in **sandbox mode** for testing purposes.

---

## Features

- **`/pay` POST endpoint**: Creates a payment on Stripe.
- **`/payments` GET endpoint**: Retrieves all payments from Stripe.
- **Stripe Sandbox**: All payments are processed in test mode.
- Easy setup via `.env` file for your Stripe API keys.

---

## Files

- **main.py**: Fastapi main service file.
- **test_payment.py**: This file can make post request to `/payments` endpoint for testing.
