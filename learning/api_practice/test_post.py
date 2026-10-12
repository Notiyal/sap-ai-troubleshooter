import requests

data = {
  "incident": "Production System Down",
  "severity": "Critical"
}

response = requests.post(
  "https://httpbin.org/post",
  json=data
)

print("Status code:", response.status_code)

result = response.json()
print("Sent data:", result["json"])