import requests
from bs4 import BeautifulSoup

class Tiobe:
 
    def __init__(self):
        self.data = []
        self.url = 'https://www.tiobe.com/tiobe-index/'
        self.headers = {}
 
    def getRank(self):
        self.headers['user-agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'
        res = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        table = soup.find('table', class_="table table-striped table-top20").find_all('td')
        i = 0
        print(len(table))
        while i < len(table):
            obj = {} 
            obj['rank'] = table[i].text
            obj['oldrank'] = table[i+1].text
            obj['name'] = table[i+3].text
            obj['ratings'] = table[i+4].text
            obj['change'] = table[i+5].text
            self.data.append(obj)
            i += 6
 
        return self.data

def main():
    print('hello')
    spider = Tiobe()
    print(spider.getRank())

if __name__ == '__main__':
    main()
