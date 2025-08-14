import requests
def test_create_product():
    url = "http://localhost:8000/product/create"
    data = {
        "name": "Test Product",
        "description": "test product",
        "active": True,
        "price": 19.99,
        "currency": "usd",
        "metadata": {
            "stock": 100
        }
    }

    response = requests.post(url, json=data)
    print("Status:", response.status_code)
    print("Response:", response.json())

def test_delete_product():
    product_id = "" 
    url = f"http://localhost:8000/product/delete/{product_id}"

    response = requests.delete(url)
    print("Status:", response.status_code)
    print("Response:", response.json())

def test_modify_product():
    product_id = "" 
    url = f"http://localhost:8000/product/modify/{product_id}"
    data = {
        "name": "Test Product Modified",
        "description": "Test product description modified",
        "active": True,
        "price": 100,
        "currency": "eur",
        "metadata": {
            "stock": 50
        }
    }

    response = requests.put(url, json=data)
    print("Status:", response.status_code)
    print("Response:", response.json())