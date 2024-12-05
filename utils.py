import os

import requests

DEFAULT_LINKEDIN_PROFILE_URL = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
PROXY_CURL_BASE_URL = "https://nubela.co/proxycurl/api/v2/linkedin"

def scrape_linkedin_profile(url: str = DEFAULT_LINKEDIN_PROFILE_URL):
    if url is DEFAULT_LINKEDIN_PROFILE_URL:
        return requests.get(url, timeout=10).json()

    headers = {"Authorization": f"Bearer {os.environ['PROXYCURL_API_KEY']}"}
    return requests.post(PROXY_CURL_BASE_URL, params={"url": url}, headers=headers, timeout=10).json()


if __name__ == "__main__":
    profile = scrape_linkedin_profile()
    print(profile)