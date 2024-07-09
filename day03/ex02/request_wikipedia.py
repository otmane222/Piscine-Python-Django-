import sys
import dewiki
import json
import requests

def starto():
    if len(sys.argv) == 1:
        print("Error: No arguments")
        return
    if len(sys.argv) > 2:
        print("Error: Too many arguments")
        return
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "action": "parse",
        "page": sys.argv[1],
        "prop": "wikitext",
        "format": "json",
        "redirects": "true",
    }
    
    response = requests.get(url=URL, params=PARAMS)
    data = response.json()
    if "error" in data:
        print("Error: Page not found")
        return
    data = data["parse"]["wikitext"]["*"]
    data = dewiki.from_string(data)
    with open (sys.argv[1] + ".wiki", "w") as file:
        file.write(data)

if __name__ == "__main__":
    starto()
