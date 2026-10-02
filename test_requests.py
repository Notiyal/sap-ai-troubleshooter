import requests

response = requests.get("https://httpbin.org/get")

print("Status code:", response.status_code)

data = response.json()

print("URL:", data["url"])
print("Origin:", data["origin"])