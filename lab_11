import requests

def get_call():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = response.json()

    filter_data = [item for item in data if len(item["title"].split()) <= 6]
    
    print(f"Filtered results for GET call to posts endpoint with more than 6 words:")
    print(filter_data)

    filter_data = [item for item in filter_data if len(item["body"].split("\n")) <= 3]

    print(f"Filtered results for GET call to posts endpoint with more than 3 lines:")
    print(filter_data)

def post_call(data):
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
    print(f"Response from POST call to posts endpoint:")
    print(response.json())

def put_call(data, id):
    response = requests.put(f"https://jsonplaceholder.typicode.com/posts/{id}", json=data)
    print(f"Response from PUT call to posts endpoint:")
    print(response.json())

def delete_call(id):
    response = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{id}")
    print(f"Response from DELETE call to posts endpoint:")
    print(response.status_code)

get_call()

new_post = {"title": "New Post Title", "body": "New Post Body"}
post_call(new_post)

updated_post = {"id": 1, "title": "Updated Post Title", "body": "Updated Post Body"}
put_call(updated_post, 1)

delete_call(2)
