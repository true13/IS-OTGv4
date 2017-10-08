from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(page_url):
    global pages
    print(page_url)
    html = urlopen(page_url)
    bsObj = BeautifulSoup(html, "html.parser")

    for link in bsObj.findAll("a", href=re.compile("^(https://iscert.org)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                pages.add(newPage)
                getLinks(newPage)


getLinks("https://www.iscert.org")