import sys
import requests
from bs4 import BeautifulSoup

def web_search(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No title found"
        
        # Extract the first paragraph or a portion of the content
        content = soup.find('p')
        content_text = content.text[:200] + "..." if content else "No content found"
        
        return f"Title: {title}\n\nContent preview: {content_text}"
    except Exception as e:
        return f"Error occurred: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python search.py <url>")
        sys.exit(1)
    url = sys.argv[1]
    result = web_search(url)
    print(result)
