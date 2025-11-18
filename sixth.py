import sys
import requests
import re


def download_url_and_get_all_hrefs(url):
    
    hrefs = []

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Stahovani URL skoncilo chybou, status code: {response.status_code}")
    
    html = response.text

    pattern = r'<a\s+[^>]*href=["\'](.*?)["\']'
    hrefs = re.findall(pattern, html, re.IGNORECASE)

    return hrefs

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        hrefs = download_url_and_get_all_hrefs(url)

        for h in hrefs:
            print(h)

    except Exception as e:
        print(f"Program skoncil chybou: {e}")
