from selenium import webdriver
from time import sleep
#1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
browser = webdriver.Chrome(executable_path ="J:\chromedriver\chromedriver.exe")
#2.通过浏览器向服务器发送URL请求
browser.get("https://qun.qq.com/member.html#gid=951192978")
sleep(20)
#browser.sleep(3)
all_number_nickname = browser.find_elements_by_xpath('//*[@class="list"]/tr/td[3]/span[1]')
all_number_name = browser.find_elements_by_xpath('//*[@class="list"]/tr/td[4]/span[1]')
all_number_order = browser.find_elements_by_class_name('td-no')
all_number_qq = browser.find_elements_by_xpath('//*[@class="list"]/tr/td[5]')
all_number_sex = browser.find_elements_by_xpath('//*[@class="list"]/tr/td[6]')
all_number_qqage = browser.find_elements_by_xpath('//*[@class="list"]/tr/td[7]')
all_number_intime = browser.find_elements_by_xpath('//*[@class="list"]/tr/td[8]')
all_number_marks = browser.find_elements_by_xpath('//*[@class="list"]/tr/td[9]')
all_number_lastsaytime = browser.find_elements_by_xpath('//*[@class="list"]/tr/td[10]')
# for i in [all_number_qq,all_number_nickname,all_number_name,all_number_order,all_number_sex,all_number_qqage,all_number_intime,all_number_marks,all_number_lastsaytime]:
#   for j in i:
#     print(j.text)
list=[]
for k in range(len(all_number_qq)):
  list.append([])
  list[k].append(all_number_qq[k].text)
  list[k].append(all_number_nickname[k].text)
  list[k].append(all_number_name[k].text)
  list[k].append(all_number_order[k].text)
  list[k].append(all_number_sex[k].text)
  list[k].append(all_number_qqage[k].text)
  list[k].append(all_number_intime[k].text)
  list[k].append(all_number_marks[k].text)
  list[k].append(all_number_lastsaytime[k].text)
import openpyxl
def write_excel_xlsx(path, sheet_name, value):
  index = len(value)
  workbook = openpyxl.Workbook()
  sheet = workbook.active
  sheet.title = sheet_name
  for i in range(0, index):
    for j in range(0, len(value[i])):
      sheet.cell(row=i+1, column=j+1, value=str(value[i][j]))
  workbook.save(path)
  print("xlsx格式表格写入数据成功！")
book_name_xlsx = 'python小白交流群成员.xlsx'
sheet_name_xlsx = 'python小白交流群成员'
value = list
write_excel_xlsx(book_name_xlsx, sheet_name_xlsx, value)