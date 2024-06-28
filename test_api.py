# Import the necessary library
import requests

# Define the URL of the API Gateway
url = "https://url_api.us-east-1.amazonaws.com/prod/hello"

# Send a GET request to the API Gateway
response = requests.get(url)

# Check if the response status code is 200
if response.status_code == 200:
    print("Success! Received 200 HTTP response.")
else:
    print(f"Failed! Received {response.status_code} HTTP response.")

# Optionally, print the response content for further inspection
print("Response content:", response.text)