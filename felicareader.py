# -*- coding: utf-8 -*-
'''
This script is for register of NFC cards.
Run this script, touch your card on censor,
and then its IDm will be written into file.
'''

import binascii
import datetime
import sys
import time

import nfc
from RPi import GPIO

def main(ids_csv_filename):
    with open(ids_csv_filename, 'a') as ids_csv_file:
        clf = nfc.ContactlessFrontend('usb')
        print "Press ^C to quit ..."
        while True:
            time.sleep(1)

            tag = clf.connect(rdwr={'on-connect': None})
            if not isinstance(tag, nfc.tag.tt3.Type3Tag):
                print "Invalid card type"
                continue

            idm = binascii.hexlify(tag.idm)
            print "ID: " + idm
            now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            ids_csv_file.write("{},{}\n".format(now, idm))



if __name__ == '__main__':
    main(sys.argv[1])
