#coding:utf-8

import binascii
import sys
import csv
import datetime
import time
import os
sys.path.insert(1, os.path.split(sys.path[0])[0])
import nfc

print "** Waiting for a Tag ... **"

def connected(tag):
	print tag
	tagdata = '%s' %tag
	index = tagdata.find('ID=')+3
	print "index = %d" % index
	idmdata = tagdata[index:index+16]
	print "idmdata = %s" %idmdata
	IDm = int(idmdata,16)
	print "IDm = %x" % IDm


clf = nfc.ContactlessFrontend('usb')
clf.connect(rdwr={'on-connect': connected})

print "%x" % IDm

f = open('Logdata.csv', 'ab')
csvWriter = csv.writer(f)

now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
listData = []	#書き込み用
listData.append(now)	#時刻を追加
listData.append(IDm)	#IDmを追加
csvWriter.writerow(listData)	#書き込み

f.close()

print "Logging complete !"
