import requests
from bs4 import BeautifulSoup

class Hh_scrap:

    def __init__(self) -> None:
        self.api_url = 'https://api.hh.ru/'
        self.site_url = 'https://hh.ru/'
        self.headers = {'User-Agent': 'Chrome/109.0.5414.120'}
    
    def test_sop(self,ret):
        self.soup = BeautifulSoup(ret)
        return self.soup

    def hh_api_get(self,param):
        rqst = requests.get(self.api_url+param, headers=self.headers, timeout=3)
        rqst.encoding = "utf-8"
        result = rqst.json()
        return result
    

    def hh_get_page(self,urls):
        rqst = requests.get(urls,headers=self.headers, timeout=3)
        result = rqst.text
        return result


    def delicious_soup(self,ret):
        soup = BeautifulSoup(ret, 'html.parser')
        return soup
        
    
    def find_soup(self, url, tag, attrs):
        self.soup = self.delicious_soup(self.hh_get_page(url))
        self.posts = self.soup.find(tag, attrs=attrs)
        if self.posts is None:
            return self.posts
        else:
            return self.posts.text
