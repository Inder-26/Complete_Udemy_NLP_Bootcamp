import threading
import requests
from bs4 import BeautifulSoup

urls = [
    "https://docs.langchain.com/oss/python/reference/overview",
    "https://langchain-doc.readthedocs.io/en/latest/getting_started/getting_started.html",
    "https://docs.langchain.com/oss/python/deepagents/overview"
]
def fetch_contents(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"Fetched {len(soup.text)} characters from {url}")
    print(soup.text)

threads = []
for url in urls:
    thread = threading.Thread(target=fetch_contents, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All docs fetched.")