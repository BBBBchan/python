import requests
import time
from bs4 import BeautifulSoup
import random
import pymysql

all_language = [  'JavaScript','PHP','C', 'Ruby','C%2B%2B', 'Java',
                'Objective-C','Python','Matlab', 'Scala', 'SQL','Go', 'R语言', '汇编', 'C%23', 'VB.NET']
all_company = [  '网易','美团','华为', '腾讯', '金山', '百度','360'\
                   '携程', '新浪', '苏宁易购','拼多多',  '唯品会', '陆金所', '科大讯飞'\
                '58', '滴滴出行','快手', '小米','汽车之家', '爱奇艺', '链家网', '哔哩哔哩', '斗鱼', '迅雷','字节跳动', '京东','阿里巴巴',  ]



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
        self.proxies = ''

    def get_it(self):
        self.headers[
            'user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36 '
        res = requests.get(self.url, headers=self.headers)
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
    def gather(self):
        i = 0
        while i < len(self.company):
            temp = [self.company[i], self.job[i], self.money[i], self.place[i]]
            self.data.append(temp)
            i += 1

    def money_trans(self):
        all_money = 0
        for i in range(len(self.money)):
            now_company_temp = now_company
            j = 0
            temp1 = ''
            temp2 = ''
            if now_company_temp == '字节跳动':
                now_company_temp = '今日头条'
            elif now_company_temp == '阿里巴巴':
                now_company_temp = '阿里'
            elif now_company_temp == '哔哩哔哩':
                now_company_temp = 'bilibili'
            if int(self.company[i].find(now_company)) == -1 and self.company[i].find(now_company_temp) \
                    or int(self.job[i].find('产品') != -1) or int(self.job[i].find('C端') != -1) or int(self.job[i].find('编辑') != -1) :
                continue
            self.count += 1

            while j < len(self.money[i]) and self.money[i][j] != '-':
                temp1 += self.money[i][j]
                j += 1
            j += 1
            while j < len(self.money[i]) and self.money[i][j] != 'K':
                temp2 += self.money[i][j]
                j += 1
            try:
                all_money += int(temp1) + (int(temp2) - int(temp1)) * 0.1
            except:
            	print('here')
            	continue
          #  all_money += int(temp2)
            if int(temp1) < self.min_money:
                self.min_money = int(temp1)
                self.min_moneyjob = self.job[i]
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
    localtime = time.asctime( time.localtime(time.time()) )
    print('开始执行时间: ', localtime)
    spider = spider()
    for now_company in all_company:
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
            spider.url = 'https://www.zhipin.com/c100010000/?query='+now_language+'+'+now_company+'&page=1&ka=page-1'
            for i in range(1,6):
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
                # Min_money.append(spider.min_money)
                # Max_money.append(spider.max_money)
                spider.renew()
                time.sleep(65)
            if count != 0:
                Average = int(All_money/count)
            else:
                Average = 0
                Min = 0
            # Min = min(Min_money)
            # Max = max(Max_money)
            if now_language == 'R语言':
                now_language = 'R'
            elif now_language == '汇编':
                now_language = 'Assembly'
            elif now_language == 'C%2B%2B':
                now_language = 'C++'
            elif now_language == 'C%23':
                now_language = 'C#'
            elif now_language == 'C':
                Max = 0.9*Max
                Min = 0.9*Min
                
           # 数据库相关
            conn = pymysql.connect(host='mysql.wizzstudio.com', port=3333, user='pgrk', passwd='wizz.pgrk', db='pgrk_rel_2')
            cursor = conn.cursor()
            # cursor.execute("insert into company_salary(language_name, company_name, company_ord_salary, company_max_salary, company_max_salary_post, company_min_salary, company_min_salary_post) values('%s', '%s', '%d', '%d', '%s', '%d', '%s')"%(now_language,now_company,Average,Max,Max_job,Min,Min_job))
            cursor.execute("update company_salary set company_ord_salary='%d',company_max_salary='%d',company_max_salary_post='%s',company_min_salary='%d',company_min_salary_post='%s' where language_name = '%s' and company_name = '%s' " % (Average,Max,Max_job,Min,Min_job,now_language,now_company))
            conn.commit()
            localtime = time.asctime( time.localtime(time.time()) )
            print('当前时间: ', localtime)
            print('写入数据: ', now_company, now_language,Max, Max_job, Min, Min_job)
            time.sleep(100)
