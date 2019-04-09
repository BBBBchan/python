import requests
import time
import pymysql
from bs4 import BeautifulSoup

all_language = ['C%2B%2B', 'Java', 'Python', 'Javascript', 'R语言', 'Go', 'Matlab', 'Scala', 'VB.NET', 'SQL', 'Objective-C', 'C', 'Ruby', 'PHP', '汇编', 'C%23']
now_company = '金山'


class spider:
    def __init__(self):
        self.data = []
        self.company = []
        self.job = []
        self.money = []
        self.place = []
        self.url = ''
        self.headers = {}
        self.status = 0
        self.max_money = 0
        self.max_moneyjob = ''
        self.min_money = 10000
        self.min_moneyjob = ''
        self.average = 0
        self.count = 0

    def get_it(self):
        self.headers[
            'user-agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                            'Chrome/60.0.3112.78 Safari/537.36 '
        res = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        self.status = res.status_code
        table_company = soup.find('div', class_="job-list").find_all('a', target='_blank')
        table_job = soup.find('div', class_='job-list').find_all('div', class_='job-title')
        table_money = soup.find('div', class_='job-list').find_all('span', class_='red')
        table_place = soup.find('div', class_='job-list').find_all('p')
        i = 0
        while i < len(table_place):
            temp = 0
            for j in table_place[i].descendants:
                if temp == 0:
                    self.place.append(j)
                    temp += 1
            i += 3
        i = 1
        while i < len(table_company):
            self.company.append(table_company[i].text)
            self.job.append(table_job[int((i - 1) / 3)].text)
            self.money.append(table_money[int((i - 1) / 3)].text)
            i += 3


    def gather(self):
        i = 0
        while i < len(self.company):
            temp = [self.company[i], self.job[i], self.money[i], self.place[i]]
            self.data.append(temp)
            i += 1

    def money_trans(self):
        all_money = 0
        for i in range(len(self.money)):
            j = 0
            temp1 = ''
            temp2 = ''
            if int(self.company[i].find('金山')) == -1 and int(self.company[i].find('jinshan') == -1) and int(self.company[i].find('金山') == -1) and int(self.company[i].find('金山') == -1) or int(self.job[i].find('产品') != -1) or int(self.job[i].find('C端') != -1) or int(self.job[i].find('编辑') != -1) :
                continue
            self.count+=1
            while self.money[i][j] != 'k':
                temp1 += self.money[i][j]
                j+=1

            if int(temp1) < self.min_money:
                self.min_money = int(temp1)
                self.min_moneyjob = self.job[i]
            j += 2
            while self.money[i][j] != 'k':
                temp2 += self.money[i][j]
                j += 1
            all_money += int(temp1) + (int(temp2) - int(temp1)) * 0.1
          #  all_money += int(temp2)
            if int(temp2) > self.max_money:
                self.max_money = int(temp2)
                self.max_moneyjob = self.job[i]
        if self.count != 0:
            all_money /= self.count
            self.average = all_money

    def renew(self):
        self.data = []
        self.company = []
        self.job = []
        self.money = []
        self.place = []
        self.headers = {}
        self.status = 0
        self.max_money = 0
        self.max_moneyjob = ''
        self.min_money = 10000
        self.min_moneyjob = ''
        self.average = 0
        self.count = 0

def set_url(page):
    now_url = spider.url
    new = 'page='+str(page)+'&ka=page-'+str(page)
    now_url = now_url[:int(now_url.find('page'))]
    now_url += new
    spider.url = now_url

if __name__ == '__main__':
    spider = spider()
    for now_language in all_language:
        print(now_language)
        Min_money = []
        Max_money = []
        Min = 10000
        Min_job = ''
        Max = 0
        Max_job = ''
        All_money = 0
        count = 0
        print(Min_money, Max_money)
        spider.url = 'https://www.zhipin.com/c100010000/?query='+now_language+'+'+now_company+'&page=1&ka=page-1'
        for i in range(11):
            print(spider.url)
            set_url(i)
            spider.get_it()
            spider.gather()
            spider.money_trans()
            Min_money.append(spider.min_money)
            Max_money.append(spider.max_money)
            All_money += spider.average*spider.count
            count += spider.count
            if spider.min_money < Min:
                Min = spider.min_money
                Min_job = spider.min_moneyjob
            if spider.max_money > Max:

                Max = spider.max_money
                Max_job = spider.max_moneyjob
                print(Max_job)
            # Min_money.append(spider.min_money)
            # Max_money.append(spider.max_money)
            spider.renew()
            time.sleep(5)
        if count != 0:
            Average = int(All_money/count)
        else:
            Average = 0
            Min = 0
        # Min = min(Min_money)
        # Max = max(Max_money)
        print(Average)
        print(Min, Min_job)
        print(Max, Max_job)

       # 数据库相关
        conn = pymysql.connect(host='47.105.192.87', port=3333, user='pgrk', passwd='wizz.pgrk', db='pgrk')
        cursor = conn.cursor()
        cursor.execute("insert into company_salary(language_name, company_name, company_ord_salary, company_max_salary, company_max_salary_post, company_min_salary, company_min_salary_post) values('%s', '%s', '%d', '%d', '%s', '%d', '%s')"%(now_language,now_company,Average,Max,Max_job,Min,Min_job))
        conn.commit()

        time.sleep(5)
