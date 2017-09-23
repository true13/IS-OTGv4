import requests
from bs4 import BeautifulSoup

def autoSearch(target):
    searchEngine = ['http://www.google.co.kr/search',
                    'http://www.bing.co.kr/search']
    title = []
    
    for url in searchEngine:
        for x in range(0, 3):
            if url == 'http://www.google.co.kr/search' :
                params = {'q' : "site:" + target,
                          'start' : str(x*10)}
                html = requests.get(url, params=params)
                soup = BeautifulSoup(html.content, 'html.parser')
                tmp = soup.find_all('h3')
                for x in range(0, len(tmp)):
                    title.append(tmp[x].find('a').text)
                    
            elif url == 'http://www.bing.co.kr/search' :
                params = {'q' : "site:" + target,
                          'start' : str(x*10)}
                html = requests.get(url, params=params)
                soup = BeautifulSoup(html.content, 'html.parser')

    return title

if __name__ == "__main__":
    print(autoSearch("jbnu.ac.kr"))
    
