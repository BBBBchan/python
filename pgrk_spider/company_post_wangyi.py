import requests
import time
import pymysql
from bs4 import BeautifulSoup


all_language = ['Java','C','Python','C++','Javascript','PHP','R语言','GO','MATLAB','Ruby', 'Scala','vb.net','SQL','Objective-C','C#','汇编']


class spider():
    def __init__(self):
        self.url = 'https://hr.163.com/position/list.do?postType=01&currentPage=1'
        self.status = 0
        self.headers = {}
        self.data = []

    def get_it(self):
        print(self.url)
        self.headers['user-agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                            'Chrome/60.0.3112.78 Safari/537.36 '
        res = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        print('hi')
        position_table = soup.find('table', class_="position-tb").find_all('div', class_='section')
        for i in range(0,len(position_table),4):
            self.data.append(str(position_table[i].text).lower())
def set_url(page):
    now_url = spider.url
    new = 'currentPage=' + str(page)
    now_url = now_url[:int(now_url.find('currentPage='))]
    now_url += new
    spider.url = now_url


if __name__ == '__main__':
    spider = spider()
    requirement = {}
    for i in all_language:
        requirement[i] = 0
    print(requirement)
    for i in range(1,20,1):
        set_url(i)
        spider.get_it()
        time.sleep(5)
    for i in spider.data:
        for j in all_language:
            if i.find(j.lower()) != -1:
                requirement[j] += 3
    print(requirement)
    # requirement = {'R语言': 0, 'PHP': 12, 'GO': 15, 'Python': 84, 'Javascript': 24, 'C#': 18, 'MATLAB': 6, 'vb.net': 0, 'C++': 66, 'Objective-C': 9, 'Java': 153, 'C\\': 0, 'SQL': 84, 'Scala': 9, 'Ruby': 3}
    requirement['C'] = requirement['C++']

    conn = pymysql.connect(host='47.105.192.87', port=3333, user='pgrk', passwd='wizz.pgrk', db='pgrk')
    cursor = conn.cursor()
    for i in all_language:
        print(i)
        cursor.execute("insert into company_post(language_name, company_name, company_post_number) values('%s','%s','%d')"%(str(i), '网易', requirement[i]))
        conn.commit()
