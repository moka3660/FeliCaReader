#coding:utf-8
import csv
import time

f = open('timedata.csv', 'ab')

csvWriter = csv.writer(f)

now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M*%S")
listData = [] #
listData.append(val)                      #
csvWriter.writerow(listData)          #

f.close()
