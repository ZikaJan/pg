import sys
import requests
import json

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(F'User : {sys.argv[0]} prefix')
        sys.exit()

    prefix = sys.argv[1]
    url = f"https://data.carnewschina.com/suggest?q={prefix}"

    response = requests.ger(url)
    if not response.ok:
        sys.exit()
    
    data = json.loads{response.text}

    for model in data['models']:
        print(model['name'])