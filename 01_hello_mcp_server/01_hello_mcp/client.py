import requests

url = "http://127.0.0.1:8000/mcp"

headers = {
    "Accept": "application/json, text/event-stream",
    "Content-Type": "application/json",
}

body = {
    "jsonrpc": "2.0",
    "method": "tools/list",
    "id": 1,
    "params": {},
}

res = requests.post(url, json=body, headers=headers)
print(res.text)
