import requests
import time
import pymysql
from bs4 import BeautifulSoup

all_language = ['C%2B%2B','Java','Python','JavaScript','Go','C','PHP']
other_language = ['R语言','Matlab','VB.NET','Objective-C','Ruby','汇编','C%23','SQL','Scala']
class spider():
    def __init__(self):
        self.data = []
        self.url = 'https://www.zhipin.com/c100010000/y_7-s_306-t_807/?query=C%2B%2B&page=1&ka=page-1'
        self.headers = {}
        self.place = []
        self.company = []
        self.job = []
        self.money = []
        self.status = 0

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
            i += 2
        i = 0
        while i < len(table_job):
            self.job.append(table_job[i].text)
            self.money.append(table_money[i].text)
            i+=1

    def renew(self):
        self.data = []
        self.company = []
        self.job = []
        self.money = []
        self.place = []
        self.headers = {}
        self.status = 0

def set_url(now_language):
    now_url = spider.url
    new = 'query='+now_language+'&page=1&ka=page-1'
    now_url = now_url[:int(now_url.find('query='))]
    now_url += new
    spider.url = now_url


if __name__ == '__main__':
    spider = spider()
    job = []
    salary = []
    language = []
    company = []
    for i in all_language:
        if i == 'C':
            spider.url = 'https://www.zhipin.com/c100010000/y_6-s_306-t_807/?query=C&page=1&ka=page-1'
        else:
            set_url(i)
        print(spider.url)
        spider.get_it()
        time.sleep(5)
        count = 0
        for j in range(len(spider.job)):
            if spider.job[j].find('产品') != -1:
                continue
            k = 0
            while k < count:
                if spider.job[j].lower() == job[len(job)-count+k].lower():
                    break
                else:
                    k += 1
            if k == count:
                job.append(spider.job[j])
                salary.append(spider.money[j])
                language.append(i)
                company.append(spider.company[j])
                print(spider.job[j])
                count += 1
            if count >= 6:
                break
        spider.renew()
    spider.url = 'https://www.zhipin.com/c100010000/?query=R%E8%AF%AD%E8%A8%80&page=1&ka=page-1'
    for i in other_language:
        if i == 'C%23':
            spider.url = 'https://www.zhipin.com/c100010000/y_6/?query=C%23&page=1&ka=page-1'
        elif i == 'SQL':
            spider.url = 'https://www.zhipin.com/c100010000/y_6-s_306/?query=SQL&ka=sel-salary-6'
        elif i == 'Scala':
            spider.url = 'https://www.zhipin.com/c100010000/s_306/?query=scala&ka=sel-scale-306'
        else:
            set_url(i)
        print(spider.url)
        spider.get_it()
        time.sleep(5)
        count = 0
        for j in range(len(spider.job)):
            if spider.job[j].find('产品') != -1:
                continue
            k = 0
            while k < count:
                if spider.job[j].lower() == job[len(job)-count+k].lower():
                    break
                else:
                    k += 1
            if k == count:
                job.append(spider.job[j])
                salary.append(spider.money[j])
                language.append(i)
                company.append(spider.company[j])
                print(spider.job[j])
                count += 1
            if count >= 6:
                break
        spider.renew()

    for i in range(len(job)):
        if language[i] == 'R语言':
                language[i] = 'R'
        elif language[i] == '汇编':
                language[i] = 'Assembly'
        elif language[i] == 'C%2B%2B':
                language[i] = 'C++'
        elif language[i] == 'C%23':
                language[i] = 'C#'
        print(company[i],language[i],job[i],salary[i])

    conn = pymysql.connect(host='mysql.wizzstudio.com', port=3333, user='pgrk', passwd='wizz.pgrk', db='pgrk_rel_2')
    cursor = conn.cursor()
    cursor.execute("delete from language_post where post_number = 0")
    for i in range(len(job)):
        cursor.execute("insert into language_post(company_name,language_name,language_post,post_salary,post_number) values('%s','%s', '%s', '%s', 0)" % (company[i],language[i],job[i],salary[i]))
    conn.commit()
