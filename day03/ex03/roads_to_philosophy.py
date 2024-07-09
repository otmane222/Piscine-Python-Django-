import sys
import requests
import bs4
import time

def starto():
    if len(sys.argv) == 1:
        print("Error: No arguments")
        return
    if len(sys.argv) > 2:
        print("Error: Too many arguments")
        return
    URL = "https://en.wikipedia.org/wiki/" + sys.argv[1]
    response = requests.get(url=URL)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    x = 0
    visited_urls = set()
    titles = []
    current_url = URL
    while True:
        if current_url in visited_urls:
            print("It's a dead end !")
            break
        titles.append(soup.find(id="firstHeading").text)
        visited_urls.add(current_url)
        title = soup.find(id="firstHeading").text
        if title == "Philosophy":
            for title2 in titles:
                print(title2)
            print( x + 1, "roads from", sys.argv[1], "to Philosophy !")
            break
        content = soup.find(id="mw-content-text")
        if not content:
            print("It's a dead end !")
            break
        paragraphs = content.find_all("p")
        found = False
        for paragraph in paragraphs:
            if paragraph.find("a"):
                found = True
                first_link = paragraph.find("a")
                break
        if not found:
            print("It's a dead end !")
            break
        current_url = "https://en.wikipedia.org" + first_link["href"]
        response = requests.get(url=current_url)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        x += 1

if __name__ == "__main__":
    starto()