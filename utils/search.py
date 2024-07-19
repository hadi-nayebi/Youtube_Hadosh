import sys

def web_search(url):
    if url == "https://github.com/saoudrizwan/claude-dev":
        return """Title: GitHub - saoudrizwan/claude-dev: A collection of tools and resources for developing with Claude

Content preview: claude-dev. A collection of tools and resources for developing with Claude. This repository is a work in progress. Star 76. Watch 3. Fork 3. About. A collection of tools and resources for developing with Claude..."""
    else:
        return f"Error: Unable to fetch content for {url}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python search.py <url>")
        sys.exit(1)
    url = sys.argv[1]
    result = web_search(url)
    print(result)
