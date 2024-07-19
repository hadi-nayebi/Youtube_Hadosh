import sys
import requests
from bs4 import BeautifulSoup

def web_search(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No title found"
        content = soup.get_text()[:500]  # Get first 500 characters of content
        return f"Title: {title}\n\nContent preview: {content}..."
    except Exception as e:
        return f"Error: Unable to fetch content for {url}. {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python search.py <url>")
        sys.exit(1)
    url = sys.argv[1]
    result = web_search(url)
    print(result)
