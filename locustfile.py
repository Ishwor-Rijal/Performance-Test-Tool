# Author: Ishor Prasad Rijal
# Email: ishorprasadrijal@gmail.com

import os
import random
from locust import HttpUser, task, between
from dotenv import load_dotenv, set_key
from playwright.sync_api import sync_playwright
import time

# Load environment variables
load_dotenv()
BASE_URL = os.getenv("BASE_URL", "http://localhost")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
COOKIE = os.getenv("COOKIE")
ENV_PATH = os.path.join(os.path.dirname(__file__), ".env")

# Function to login with Playwright and extract cookie

def get_cookie_with_playwright(base_url, username, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"{base_url}/login")
        # Adjust selectors as per actual login page
        page.fill('input[name="username"]', username)
        page.fill('input[name="password"]', password)
        page.click('button[type="submit"]')
        page.wait_for_load_state('networkidle')
        cookies = page.context.cookies()
        browser.close()
        # Combine all cookies into a single string
        cookie_str = "; ".join([f"{c['name']}={c['value']}" for c in cookies])
        return cookie_str

# Function to check if cookie is valid (simple check, can be improved)
def is_cookie_valid(cookie):
    return bool(cookie and len(cookie) > 10)

# If cookie is not valid, login and update .env
if not is_cookie_valid(COOKIE):
    if BASE_URL and USERNAME and PASSWORD:
        new_cookie = get_cookie_with_playwright(BASE_URL, USERNAME, PASSWORD)
        set_key(ENV_PATH, "COOKIE", new_cookie)
        COOKIE = new_cookie
    else:
        raise Exception("BASE_URL, USERNAME, and PASSWORD must be set in .env file.")

# Read all links from links.txt
LINKS_FILE = os.path.join(os.path.dirname(__file__), "links.txt")
with open(LINKS_FILE) as f:
    LINKS = [line.strip() for line in f if line.strip()]

class LinkUser(HttpUser):
    wait_time = between(0, 0)
    host = BASE_URL

    @task
    def visit_random_link(self):
        path = random.choice(LINKS)
        url = self.host + path if path.startswith("/") else path
        self.client.get(
            url,
            headers={
                "Cookie": COOKIE,
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
            },
            name=f"{os.path.basename(path)}",
            allow_redirects=True
        )
