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
		
		
	def web_sever (self):
		req = requests.get(self.url)
		status = req.status_code
		
		if  200 != status:
			print("Connect Error: ", end=' ')
			print(status)
		else:
			print(req.headers['Server'])
			
		
			
	#framework check	
	def framework (self):		
		req = requests.get(self.url)
		
		#HTTP headers
		if  req.headers['Accept-Encoding'] != ''
			print(req.headers['Accept-Encoding'])
		
		#cookies
		cooki = req.cookies
		framework_type_cooki = ['zope3' , 'cakephp', 'accuracy', 'kohanasession', 'laravel_session']
		framework_type_cooki_result = []
		
		for x in range(1,4)
			if cooki == framework_type_cooki[x]
				framework_type_result[x] =1
			else
				framework_type_result[x] =0
				
		#HTML Source
		soup = BeautifulSoup(url, 'html.parser')	
		framework_type_html = ['<!- START header.Tags.cfm' ,'_ _VIEWSTATE' ,'<!-ZK' ,'<!- BC_OBNW ->' ,'ndxz-studio' ]
		framework_type_html_result = [] 
		for x in range(0,4)
			if 	'' !=soup.find_all(framework_type_html[x])
				framework_type_html_result[x]= 1
			else
				framework_type_html_result[x]= 0
		




if __name__ == "__main__":
    IG = InformationGathering("jbnu.ac.kr")