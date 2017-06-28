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

class FeliCaManager(object):
    _LED_RED = 17
    _LED_GREEN = 27
    _LED_BLUE = 22

    @property
    def __enter__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._LED_RED,GPIO.OUT)
        GPIO.setup(self._LED_GREEN,GPIO.OUT)
        GPIO.setup(self._LED_BLUE,GPIO.OUT)
        GPIO.output(self._LED_RED,0)
        GPIO.output(self._LED_GREEN,0)
        GPIO.output(self._LED_BLUE,0)
        print "Started FeliCaReader !!"
        return self

    def __exit__(self):
        GPIO.cleanup()
        print "Stopped FeliCaReader."

    def read(self):
        GPIO.output(self._LED_BLUE, 1)
        time.sleep(0.5)
        GPIO.output(self._LED_BLUE, 0)
        print "Successfully get IDm."

def main(ids_csv_filename):
    with open(ids_csv_filename, 'a') as ids_csv_file, FeliCaManager() as felica_manager:
        clf = nfc.ContactlessFrontend('usb')
        print "Press ^C to quit ..."
        while True:
            time.sleep(1.0)

            tag = clf.connect(rdwr={'on-connect': None})
            if not isinstance(tag, nfc.tag.tt3.Type3Tag):
                print "Invalid card type"
                continue

            idm = binascii.hexlify(tag.idm)
            felica_manager.read()
            print "ID: " + idm
            now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            ids_csv_file.write("{},{}\n".format(now, idm))



if __name__ == '__main__':
    main(sys.argv[1])
