import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(API_URL)
if response.status_code == 200:
    json_data = response.json()
    print("Data fetched successfully")
    
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    


print(response)