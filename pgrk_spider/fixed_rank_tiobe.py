import requests
import pymysql
from bs4 import BeautifulSoup

all_language = ['Java','C','Python','C++','Javascript','PHP','R','GO','MATLAB','Ruby', 'Scala','vb.net','SQL','Objective-C','C#','Assembly']

class Tiobe:

    def __init__(self):
        self.data = []
        self.url = 'https://www.tiobe.com/tiobe-index/'
        self.headers = {}

    def getRank(self):
        self.headers[
            'user-agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'
        res = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        table = soup.find('table', class_="table table-striped table-top20").find_all('td')
        table2 = soup.find('table', class_ = "table table-striped").find_all('td')
        i = 0
        print(len(table))
        while i < len(table):
            obj = {}
            obj['rank'] = table[i].text
            obj['oldrank'] = table[i + 1].text
            obj['name'] = table[i + 3].text
            obj['ratings'] = table[i + 4].text
            obj['change'] = table[i + 5].text
            self.data.append(obj)
            i += 6
        i = 0
        while i < len(table2):
            obj={}
            obj['rank'] = table2[i].text
            obj['name'] = table2[i + 1].text
            obj['ratings'] = table2[i + 2].text
            self.data.append(obj)
            i += 3
        return self.data


def main():
    print('hello')
    language = []
    rating = []
    spider = Tiobe()
    data = spider.getRank()
    count = 0
    for i in data:
        rating.append(float(i['ratings'][0:i['ratings'].find('%')-1])/100)
        if i['name'].find('Visual Basic .NET') != -1:
            language.append('VB.NET')
        elif i['name'].find('Assembly language') != -1:
            language.append('Assembly')
        else:
            language.append(i['name'])
        print(language[count],rating[count])
        count+=1


    conn = pymysql.connect(host='47.105.192.87', port=3333, user='pgrk', passwd='wizz.pgrk', db='pgrk')
    cursor = conn.cursor()
    i= 0
    while i < len(language):
        cursor.execute("update fixed_rank set tiobeexponent = '%f' where language_name = '%s' " %(rating[i], language[i]))
        i+=1
    conn.commit()


if __name__ == '__main__':
    main()
