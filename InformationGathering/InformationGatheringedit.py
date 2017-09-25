import requests
from bs4 import BeautifulSoup


class InformationGathering:
    def __init__(self, target_url):
        self.url = target_url
        self.search_engine()

    def search_engine(self):
        search_engine = ['http://www.google.com/search', 'http://www.bing.com/search']
        title_google = []
        title_bing = []

        for url in search_engine:
            for x in range(0, 2):
                if url == 'http://www.google.com/search':
                    params = {'q': "site:" + self.url,
                              'start': str(x * 10)}
                    html = requests.get(url, params=params)
                    soup = BeautifulSoup(html.content, 'html.parser')
                    tmp = soup.find_all('h3')
                    for y in range(0, len(tmp)):
                        title_google.append(tmp[y].find('a').text)

                elif url == 'http://www.bing.com/search':
                    params = {'q': "site:" + self.url,
                              'start': str(x * 10)}
                    html = requests.get(url, params=params)
                    soup = BeautifulSoup(html.content, 'html.parser')
                    tmp = soup.find_all('h2')
                    for y in range(0, len(tmp)):
                        title_bing.append(tmp[y].find('a').text)

        print("Google" + str(title_google))
        print("Bing" + str(title_bing))
		
		
	def websever (self):
		req = requests.get(self.url)
		status = req.status_code
		
		if  200 != status:
			print("Connect Error: ", end=' ')
			print(status)
		else:
			print(req.headers['Server'])
			
		
	def framework (self):
		pass
		
	
	
	

if __name__ == "__main__":
    IG = InformationGathering("jbnu.ac.kr")