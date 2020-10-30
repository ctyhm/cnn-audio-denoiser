import requests
import re
import time
from lxml import etree
import csv
import random
from bs4 import BeautifulSoup

import sys

# sys.setdefaultencoding("utf-8")

fp = open('智联招聘.csv', 'wt', newline='', encoding='UTF-8')
writer = csv.writer(fp)
'''''地区，公司名，学历，岗位描述，薪资，福利，发布时间，工作经验，链接'''
writer.writerow(('职位', '公司', '地区', '学历', '岗位', '薪资', '福利', '工作经验', '链接'))


def info(url):
    res = requests.get(url)
    u = re.findall('<meta name="mobile-agent" content="format=html5; url=(.*?)" />', res.text)

    if len(u) > 0:
        u = u[-1]
    else:
        return

    u = 'http:' + u

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
    }

    res = requests.get(u, headers=headers)
    selector = etree.HTML(res.text)
    print(selector)
    # # 岗位名称
    # title = selector.xpath('//*[@id="r_content"]/div[1]/div/div[1]/div[1]/h1/text()')
    # # 岗位薪资
    # pay = selector.xpath('//*[@id="r_content"]/div[1]/div/div[1]/div[1]/div[1]/text()')
    # # 工作地点
    # place = selector.xpath('//*[@id="r_content"]/div[1]/div/div[1]/div[3]/div[1]/span[1]/text()')
    # # 公司名称
    # companyName = selector.xpath('//*[@id="r_content"]/div[1]/div/div[1]/div[2]/text()')
    # # 学历
    # edu = selector.xpath('//*[@id="r_content"]/div[1]/div/div[1]/div[3]/div[1]/span[3]/text()')
    # # 福利
    # walfare = selector.xpath('//*[@id="r_content"]/div[1]/div/div[3]/span/text()')
    # # 工作经验
    # siteUrl = res.url
    # workEx = selector.xpath('//*[@id="r_content"]/div[1]/div/div[1]/div[3]/div[1]/span[2]/text()')
    # # 岗位详细
    comment = selector.xpath('//*[@class="content content-word"]/text()')
    print(comment)
    content_list = selector.xpath('.//div[@id="job-view-enterprise"]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/text()').extract()
    content = ''
    for value in content_list:
        content += value.strip(' ')
    print(content)
    # writer.writerow((title, companyName, place, edu, comment, pay, walfare, workEx, siteUrl))
    # print(title, companyName, place, edu, comment, pay, walfare, workEx, siteUrl)
    return content


def infoUrl(url):
    # res = requests.get(url)
    # selector = res.status_code

    # hea是我们自己构造的一个字典，里面保存了user-agent。
    # 让目标网站误以为本程序是浏览器，并非爬虫。
    # 从网站的Requests Header中获取。【审查元素】
    hea = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'
    }

    html = requests.get(url, headers=hea)

    html.encoding = 'utf-8'  # 这一行是将编码转为utf-8否则中文会显示乱码。

    # time.sleep(3)
    code = html.status_code
    # 请求成功再解析报文
    if code == 200:
        # soup 得到html格式对象
        soup = BeautifulSoup(html.text, 'html.parser')  # 文档对象
        # selector = etree.HTML(res.text)
        sojob_list = soup.findAll('ul', class_='sojob-list')
        for k in sojob_list[0].find_all('li'):  # 遍历li
            print('==============k.children()==================')
            l = list()
            for div in k.findAll('div',attrs = {'class':'job-info'}): #从li中获取div图层
                print('*************************************')

                h3 = div.find('h3') # 取招聘岗位
                # pa = re.compile(r'<span class="text-warning">(.+?)</span>')
                a = h3.find('a')

                url = a['href'] # 招聘岗位详细链接
                title = h3['title'] # 招聘岗位名称（标题）
                p = div.find('p',class_='condition clearfix')

                p_lists = p['title'].split('_')

                # salary = p.find('span',class_='text-warning').string
                # area = p.find('a',class_='area').text
                # edu = p.find('span',class_='edu').string
                # year = p('span')[2].string

                salary = p_lists[0]
                area = p_lists[1]
                edu = p_lists[2]
                year = p_lists[3]
                l.append(url)
                l.append(title)
                l.append(salary)
                l.append(area)
                l.append(edu)
                l.append(year)
                # print(url)
                # print(title)
                # print(salary)
                # print(area)
                # print(edu)
                # print(year)

            for div in k.findAll('div', attrs={'class': 'company-info nohover'}):  # 从li中获取div图层
                p = div.find('p',class_='company-name')  # 取招聘岗位
                company = p.find('a')
                company_name = company['title']
                l.append(company_name)
            print(l[0])
            # 将获取的url传递到获取详情的函数中返回详情信息
            infos = info(l[0])
            print(infos)
            l.append(infos)
            print(l)
            # for li in k.find_all_next('li'):
            #     print('==============li==================')
            #     print(li)


        # for i in data:
        #     # href = i['positionURL']
        #     # info(href)
        #     print(len(data))
        #     print(data.count('http'))
        #     print(i)
        #     time.sleep(random.randrange(1, 4))


if __name__ == '__main__':
    # 设置关键词搜索
    key = '%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD'
    # 设置页数(因为本网站人工智能关键词总共10页，这里仅设置10)
    pageNum = 1

    # url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=' + key + '&kt=3&lastUrlQuery=%7B%22pageSize%22:%2260%22,%22jl%22:%22489%22,%22kw%22:%22%E5%A4%A7%E6%95%B0%E6%8D%AE%22,%22kt%22:%223%22%7D'
    # url = 'https://www.liepin.com/zhaopin/?sfrom=click-pc_homepage-centre_searchbox-search_new&d_sfrom=search_fp&key=' + key
    # infoUrl(url)

    urls = ['https://www.liepin.com/zhaopin/?sfrom=click-pc_homepage-centre_searchbox-search_new&d_sfrom=search_fp&key='+ key
            + '&siTag=8Gjw2tdHib7iEBY8QKS1DQ~fA9rXquZc5IkJpXC-Ycixw&d_sfrom=search_fp&d_ckId=d98adea730cc45d80c8175de1b40a03f&d_curPage=2&d_pageSize=40&d_headId=d98adea730cc45d80c8175de1b40a03f&curPage={}'.format(i) for i in range(0, pageNum)]

    # 先将所有的分页网址打印出来看看
    # for url in urls:
    print(urls)

    for url in urls:
        infoUrl(url)