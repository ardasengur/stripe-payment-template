import requests

url = "http://localhost:8000/pay"
data = {
    "amount": 5000, 
    "currency": "usd",
    "source": "tok_visa"
}

response = requests.post(url, json=data)
print("Status:", response.status_code)
print("Response:", response.json())
