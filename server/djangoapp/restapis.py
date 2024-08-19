# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    params = "&".join(f"{key}={value}" for key, value in kwargs.items())
    request_url = f"{backend_url}{endpoint}?{params}"

    print(f"GET from {request_url}")
    
    try:
        response = requests.get(request_url)
        response.raise_for_status()  
        # Raise an exception for HTTP error responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return None


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")


def post_review(data_dict):
    request_url = f"{backend_url}/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        response.raise_for_status()
        # Raise an HTTPError for bad responses (4xx and 5xx)
        response_data = response.json()
        print(response_data)
        return response_data
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return None

