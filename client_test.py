import requests

url = 'http://localhost:8000/items'
data = {'name': 'My Item', 'description': 'This is my item.'}

response = requests.post(url, json=data)

if response.status_code == 200:
    print('Item created successfully.')
else:
    print('Error creating item. Code: {}.'.format(response.status_code))
