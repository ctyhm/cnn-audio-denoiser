'''
    # 提取excel文件中的某一列，过滤关键词，如果存在就将其填入至匹配列中
'''
import xlrd
import os
import csv

def excel():
    wb = xlrd.open_workbook('E:/python_demo/cnn-audio-denoiser/zhilian/猎聘配置文件(1).xls') # 打开Excel文件
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


if __name__ == '__main__':
    '''
    # 先去读配置文件 取出搜索的关键词
    # 将返回的搜索关键词 赋值给search_keys
    # 将要提取的关键词   赋值给key_words
    '''
    search_keys,key_words = excel()
    print(search_keys)
    print(key_words)

    excel_path = './data/'
    # 获取文件名
    file_names = os.listdir(excel_path)
    print(file_names)
    # 文件名拼接路径
    file_list = [os.path.join(excel_path, file) for file in file_names]
    print(file_list)

    '''
    # 先要打开文件，然后将第一行写入，所以这个writerow必须写在获取列key_words之后
    '''
    fp = open('职位信息.csv', 'wt', newline='', encoding='utf-8')
    writer = csv.writer(fp)
    first_row = ['job_name', 'company_name', 'min_salary', 'max_salary', 'workarea', 'companytype', 'need_num', 'need_degree','need_experience','content']
    for kw in key_words:
        first_row.append(kw)
    writer.writerow(first_row)

    for file in file_list:
        wb = xlrd.open_workbook(file)  # 打开Excel文件
        sheet = wb.sheet_by_name('Sheet1')  # 通过excel表格名称(Sheet1)获取工作表
        nrows = sheet.nrows  # 总行数
        for i in range(1, nrows):  # 循环读取表格内容（每次读取一行数据）
            print('正在读取文件{}的第{}行'.format(file,i))
            wr_row = []
            cells = sheet.row_values(i)  # 每行数据赋值给cells
            for ce in range(10):
                wr_row.append(cells[ce])
                # print(cells[ce])
            w = [0] * len(key_words)  # 新建一个列表[1,len(key_words)],初始值都为0，长度是key_words的长度
            j = 0  # list的第一个索引
            for key in key_words:
                keys = key.split('_')
                for ks in keys:
                    if cells[9].lower().find(ks) != -1:
                        w[j] = 1
                j = j + 1  # 每次for循环之后索引加一
            for wi in w:
                wr_row.append(wi)
            writer.writerow(wr_row)