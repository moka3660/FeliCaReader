import binascii
import os
import sys
import datetime
import time
#import string
#import struct
#import hmac, hashlib
sys.path.insert(1, os.path.split(sys.path[0])[0])
#from cli import CommandLineInterface

import nfc
#import nfc.clf
#import ndef
from RPi import GPIO

class Maneger(object):

	def __enter__(self):
		GPIO.setmode(GPIO.BCM)
		print "Sterted"
		return self

	def __exit__(self,type,value,traceback):
		GPIO.cleanup()
		print "Stopped"

	def Check(self):
		time.sleep(0.5)
		print "Sucessfully"

def main(registered_ids_csv_filename, log_csv_filename):
	with open(registered_ids_csv_filename) as registered_ids_csv_file:
		registered_ids = [l.rstrip().split(',') for l in registered_ids_csv_file]

	if not registered_ids:
		print "No one is registered."
		return

	name_by_id = {t[0]:t[1] for t in registered_ids}

	with open(log_csv_filename, 'a') as log_csv_file, Maneger() as manager:
		clf = nfc.ContactlessFrontend('usb')
		print "Press ^C to quit ..."

		while True:
			time.sleep(1.0)

			tag = clf.connect(rdwr={'on-connect':None})
			if not isinstance(tag, nfc.tag.tt3.Type3Tag):
				print "Invalid card type."
				continue

			idm = binascii.hexlify(tag.idm)

			if idm not in name_by_id:
				print "Invalid ID: {}".format(idm)
				continue

			name = name_by_id[idm]

			print "Reading, {} ({})!".format(name, idm)
			maneger.Check()

			#logging
			now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M*%S")
			log = "{},{},{},{}\n".format(now, idm, name)
			log_csv_file.write(log)

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])
