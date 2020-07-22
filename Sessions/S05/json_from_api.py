import json
import requests

# POST
payload = {'userId': 6622, 'title': 'Something', 'body': 'some body'}

response = requests.post('https://jsonplaceholder.typicode.com/posts', data=json.dumps(payload))
assert response.status_code == 201, f'POST: Received status code {response.status_code}'
print(response.text)

# GET
data = requests.get('https://jsonplaceholder.typicode.com/todos')
assert data.status_code == 200, f'GET: Received status code {data.status_code}'

json_data = json.loads(data.text)

print(json_data)
print(type(json_data))
