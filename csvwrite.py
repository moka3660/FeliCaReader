#coding:utf-8
import csv

f = open('writedata.csv', 'ab') #ファイルが無ければ作る、の'a'を指定します

csvWriter = csv.writer(f)

val = 0
for num in range(1, 5):
   listData = [] #　　　　　　　　　　　#listの初期化
   val = num
   listData.append(val)                      #listにデータの追加
   for loop in range(0, 5):
      val = val * 10 + num
      listData.append(val)
   csvWriter.writerow(listData)          #1行書き込み

f.close()
