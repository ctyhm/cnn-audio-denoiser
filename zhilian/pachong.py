import requests
import re
import time
import xlrd
from lxml import etree
import csv
from bs4 import BeautifulSoup


key_words = []
'''
# key_words = ['java','c++','python','scala','hadoop','storm','spark','tensorflow','caffee','torch','mxnet','sql','hive',
            'cuda','图像','语言','语音','知识图谱','挖掘','cnn','rnn','lstm','word2vec','神经网络','算法','数据库','数据结构','深度学习','机器学习','人工智能']
'''



def excel():
    wb = xlrd.open_workbook('E:/python_demo/cnn-audio-denoiser/zhilian/猎聘配置文件.xls') # 打开Excel文件
    sheet = wb.sheet_by_name('Sheet1') # 通过excel表格名称(rank)获取工作表
    nrows = sheet.nrows  # 总行数
    # ncols = sheet.ncols  # 总列数
    search = sheet.row_values(0) # 第0行的数据，即搜索关键字
    searchs = []
    for se in search:
        if se != '':
            searchs.append(se)
    dat = []  #创建空list
    for i in range(1, nrows):  # 循环读取表格内容（每次读取一行数据）
        cells = sheet.row_values(i)  # 每行数据赋值给cells
        for ce in cells:
            if ce != '':
                dat.append(ce)  # 把每次循环读取的数据插入到list
        # data = int(cells[0]) # 因为表内可能存在多列数据，0代表第一列数据，1代表第二列，以此类推
    return searchs,dat


def info(url):
    heal = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.119 Safari/537.36'
    }
    time.sleep(6)
    html = requests.get(url, headers=heal)

    html.encoding = 'utf-8'  # 这一行是将编码转为utf-8否则中文会显示乱码。
    selector = etree.HTML(html.text)
    print(selector)
    '''
    # 岗位名称
    title = selector.xpath('//*[@id="r_content"]/div[1]/div/div[1]/div[1]/h1/text()')
    # 岗位薪资
    pay = selector.xpath('//*[@id="r_content"]/div[1]/div/div[1]/div[1]/div[1]/text()')
    # 工作地点
    place = selector.xpath('//*[@id="r_content"]/div[1]/div/div[1]/div[3]/div[1]/span[1]/text()')
    # 公司名称
    companyName = selector.xpath('//*[@id="r_content"]/div[1]/div/div[1]/div[2]/text()')
    # 学历
    edu = selector.xpath('//*[@id="r_content"]/div[1]/div/div[1]/div[3]/div[1]/span[3]/text()')
    # 福利
    walfare = selector.xpath('//*[@id="r_content"]/div[1]/div/div[3]/span/text()')
    # 工作经验
    siteUrl = res.url
    workEx = selector.xpath('//*[@id="r_content"]/div[1]/div/div[1]/div[3]/div[1]/span[2]/text()')
    '''

    # # 岗位详细
    comment = selector.xpath('//*[@class="content content-word"]/text()')
    print(comment)
    # content_list = selector.xpath('.//div[@id="job-view-enterprise"]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/text()')
    content = ''
    for value in comment:
        # time.sleep(1)
        value = value.replace('\uf02d','')
        value = value.replace('\xa0','')
        value = value.replace('\u2022','')
        value = value.replace('\u200b','')
        value = value.replace('\ufeff','')
        value = value.replace('\uf0a7','')
        value = value.replace('\u2f5a','')
        value = value.replace('\u2f20','')
        value = value.replace('\u2f63','')
        # value.decode('unicode-escape')
        content += value.strip()
    print(content)
    return content


def infoUrl(url):
    # res = requests.get(url)
    # selector = res.status_code

    '''
    # hea是我们自己构造的一个字典，里面保存了user-agent。
    # 让目标网站误以为本程序是浏览器，并非爬虫。
    # 从网站的Requests Header中获取。【审查元素】
    '''
    heqa = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.120 Safari/537.36'
    }
    time.sleep(3)
    html = requests.get(url, headers=heqa)

    html.encoding = 'utf-8'  # 这一行是将编码转为utf-8否则中文会显示乱码。

    code = html.status_code
    # 请求成功再解析报文
    if code == 200:
        # soup 得到html格式对象
        soup = BeautifulSoup(html.text, 'html.parser')  # 文档对象
        print(soup)
        # selector = etree.HTML(res.text)
        time.sleep(1)
        for sojob in soup.findAll('ul',attrs = {'class':'sojob-list'}):
            time.sleep(1)
            for k in sojob.find_all('li'):  # 遍历li
                time.sleep(1)
                print('==============k.children()==================')
                l = list()
                for div in k.findAll('div',attrs = {'class':'job-info'}): #从li中获取div图层
                    print('*************************************')
                    time.sleep(1)
                    h3 = div.find('h3') # 取招聘岗位
                    # pa = re.compile(r'<span class="text-warning">(.+?)</span>')
                    a = h3.find('a')
                    # time.sleep(1)
                    url = a['href'] # 招聘岗位详细链接
                    title = h3['title'] # 招聘岗位名称（标题）
                    p = div.find('p',class_='condition clearfix')
                    # time.sleep(1)
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

                for div in k.findAll('div', attrs={'class': 'company-info nohover'}):  # 从li中获取div图层
                    # time.sleep(1)
                    p = div.find('p',class_='company-name')  # 取招聘岗位
                    # time.sleep(1)
                    company = p.find('a')
                    company_name = company['title'][2:]
                    l.append(company_name)
                print(l[0])
                # 将获取的url传递到获取详情的函数中返回详情信息
                infos = ''
                if(l[0].startswith('http')):
                    infos = info(l[0])
                else:
                    l[0] = 'https://www.liepin.com' + l[0]
                    infos = info(l[0])
                # print(infos)
                w = [0] * len(key_words)  # 新建一个列表,初始值都为0，长度是key_words的长度
                i = 0  # list的第一个索引
                for key in key_words:
                    keys = key.split('_')
                    for ks in keys:
                        if infos.lower().find(ks) != -1:
                            w[i] = 1
                    i = i+1 # 每次for循环之后索引加一
                l.append(infos)
                print(l)
                row = [l[1], l[6], l[3], l[4], l[2], l[5], l[7], l[0]]
                for a in w:
                    row.append(a)
                writer.writerow(row)


def filter_emoji(desstr, restr=''):
    # 过滤表情
    try:
        res = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        res = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return res.sub(restr, desstr)

if __name__ == '__main__':
    '''
    # 先去读配置文件 取出搜索的关键词
    # 将返回的搜索关键词 赋值给search_keys
    # 将要提取的关键词   赋值给key_words
    '''
    search_keys,key_words = excel()
    print(search_keys)
    print(key_words)


    # 设置页数(因为本网站人工智能关键词总共10页，这里仅设置10)
    pageNum = 1
    startPage = 0

    '''
        # 先要打开文件，然后将第一行写入，所以这个writerow必须写在获取列key_words之后
    '''
    fp = open('猎聘.csv', 'wt', newline='',encoding='utf-8')
    writer = csv.writer(fp)
    first_row = ['职位', '公司', '地区', '学历', '薪资', '工作经验', '工作内容', '链接']
    for kw in key_words:
        first_row.append(kw)
    writer.writerow(first_row)


    for search_key in search_keys:
        # key = '%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD'

        urls = ['https://www.liepin.com/zhaopin/?sfrom=click-pc_homepage-centre_searchbox-search_new&d_sfrom=search_fp&key='+ search_key
            + '&siTag=8Gjw2tdHib7iEBY8QKS1DQ~fA9rXquZc5IkJpXC-Ycixw&d_sfrom=search_fp&d_ckId=d98adea730cc45d80c8175de1b40a03f&d_curPage=2&d_pageSize=40&d_headId=d98adea730cc45d80c8175de1b40a03f&curPage={}'.format(i) for i in range(startPage, pageNum)]

        # # 先将所有的分页网址打印出来看看
        # print(urls)

        for url in urls:
            infoUrl(url)
