# -*- coding: utf-8 -*-
'''
###
'''

import binascii
import datetime
import sys
import time

import nfc
from RPi import GPIO

#finIDm = 83598074057322759

def main(ids_csv_filename):
    with open(ids_csv_filename, 'a') as ids_csv_file:
        clf = nfc.ContactlessFrontend('usb')
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17,GPIO.OUT) #Red
        GPIO.setup(27,GPIO.OUT) #Green
        GPIO.setup(22,GPIO.OUT) #Blue
        GPIO.output(17,1)
        GPIO.output(27,1)
        GPIO.output(22,1)
        print "Started FeliCaReader !!"

        print "Press ^C to quit ..."
        while True:
            time.sleep(1.0)

            tag = clf.connect(rdwr={'on-connect': None})
            if not isinstance(tag, nfc.tag.tt3.Type3Tag):
                GPIO.output(17, 0)
                time.sleep(0.5)
                GPIO.output(17, 1)
                print "Invalid card type"
                continue

            idm = binascii.hexlify(tag.idm)

            GPIO.output(22, 0)
            time.sleep(0.5)
            GPIO.output(22, 1)
            print "Successfully get IDm."
            print "ID: " + idm

#            if idm == "12900016417f107" :
#                break

            now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            ids_csv_file.write("{},{}\n".format(now, idm))

        GPIO.cleanup()
        print "Stopped FeliCaReader."

if __name__ == '__main__':
    main(sys.argv[1])
