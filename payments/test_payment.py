import requests

url = "http://localhost:8000/pay"
data = {
    "product_id": "prod_SrgeBosClUdVO1",
    "source": "tok_visa"
}

response = requests.post(url, json=data)
print("Status:", response.status_code)
print("Response:", response.json())
