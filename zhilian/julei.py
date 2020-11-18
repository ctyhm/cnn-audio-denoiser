# 聚类
import wordcloud #导入词云库
import numpy as np
import matplotlib.pyplot as plt
import PIL
import jieba
import re

import xlrd
from sklearn import cluster

# 先读取数据，将数据放入矩阵X中
def excel():
    wb = xlrd.open_workbook('E:/python_demo/cnn-audio-denoiser/zhilian/职位信息.xlsx') # 打开Excel文件
    sheet = wb.sheet_by_name('职位信息1') # 通过excel表格名称(rank)获取工作表
    nrows = sheet.nrows  # 总行数
    # ncols = sheet.ncols  # 总列数
    first_row = sheet.row_values(0) # 第0行的数据，即关键字
    first_col = sheet.col_values(0)
    print("打印出文件首行")
    print(first_row)
    print(first_col)
    dat = []  #创建空list
    for i in range(1, nrows):  # 循环读取表格内容（每次读取一行数据）
        cells = sheet.row_values(i)  # 每行数据赋值给cells
        # 定义需要存储的列
        cols = [4, 7, 12, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
           38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62,
           63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88,
           89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111,
           112, 113, 114, 115, 116, 117, 118]
        for j in cols:
            k = int(j)
            dat.append(cells[k])  # 把每次循环读取的数据插入到list, 因为表内可能存在多列数据，0代表第一列数据，1代表第二列，以此类推
        # print(dat)
        # if(i==2):
        #     break
    # return dat
    # 将列表变形（nrows * cols）
    y = np.array(dat)
    y = y.reshape(nrows-1, len(cols))
    # 归一化，将某些列归一化，除以该列的最大值
    gyclos = [0, 1, 2, 3]
    for l in gyclos:
        # 计算每一列的最大值
        max = float(y[0][l].strip())
        for m in range(nrows-1):
            if(float(y[m][l].strip())>float(max)):
                max = float(y[m][l].strip())
        # 归一化
        for n in range(nrows-1):
            y[n][l] = float(y[n][l].strip())/float(max)
    # print(y)
    return y, first_col
if __name__ == '__main__':
    # 读数据
    print("开始读取数据")
    X, first_col = excel()
    # 聚类
    print("开始聚类")
    n_clusters = 10

    km = cluster.KMeans(n_clusters=n_clusters, init='k-means++', max_iter=1, n_init=1)
    km.fit(X)

    # 聚类完成，打印出每一行数据的类别
    # for i, j in enumerate(km.labels_):
    #     if(i%100 == 0):
    #         print(i, j)


    # 总共分n 类
    data = []
    for i in range(n_clusters):
        text = ""
        for j, k in enumerate(km.labels_):
            if (i==k):
                text = text + str(first_col[j+1])
        data.append(text)
        # with open(r'E:\master\txt1.txt',encoding='utf8') as f:
        #     text1 = f.readlines()
        #导入图片
        image1 = PIL.Image.open(r'E:\picture\master.jpg')
        MASK = np.array(image1)
        WC = wordcloud.WordCloud(font_path = 'C:\\Windows\\Fonts\\STFANGSO.TTF',
                             max_words=2000,
                             mask=MASK,
                             height=400,
                             width=400,
                             background_color='white',
                             repeat=False,
                             mode='RGBA') # 设置词云图对象属性
        st1 = re.sub('[，。、“”‘ ’]', '', str(text)) # 使用正则表达式将符号替换掉。
        conten = ' '.join(jieba.lcut(st1)) # 此处分词之间要有空格隔开，联想到英文书写方式，每个单词之间都有一个空格。
        con = WC.generate(conten)
        plt.imshow(con)
        plt.axis("off")
        plt.show()