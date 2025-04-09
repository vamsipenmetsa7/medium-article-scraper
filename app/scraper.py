import requests
from bs4 import BeautifulSoup

def scrape_medium_headers_with_titles(article_url):
    try:
        # Fetch the Medium article
        response = requests.get(article_url)
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all headers (h1, h2, h3, etc.)
        headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

        # Construct a hierarchy of headers
        header_hierarchy = []
        stack = []

        for header in headers:
            header_id = header.get('id')
            header_text = header.get_text(strip=True)
            if header_id:
                level = int(header.name[1])  # Extract the header level (e.g., 1 for h1, 2 for h2)
                header_data = {"text": header_text, "link": f"{article_url}#{header_id}", "children": []}

                # Adjust the stack to maintain hierarchy
                while stack and stack[-1]["level"] >= level:
                    stack.pop()

                if stack:
                    stack[-1]["data"]["children"].append(header_data)
                else:
                    header_hierarchy.append(header_data)

                stack.append({"level": level, "data": header_data})

        return header_hierarchy
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the article: {e}")
        return []