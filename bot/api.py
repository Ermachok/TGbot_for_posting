import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL", "http://localhost:8000")


def get_posts():
    resp = requests.get(f"{API_URL}/posts")
    resp.raise_for_status()
    return resp.json()


def get_post(post_id: int):
    resp = requests.get(f"{API_URL}/posts/{post_id}")
    resp.raise_for_status()
    return resp.json()
