# -*- coding: utf-8 -*-

import binascii
import nfc
import sys
import time
import datetime
from RPi import GPIO

finIDm = 72340248454488070  #010101129C17E006 [ICOCA]

class MyCardReader(object):

    def on_connect(self, tag):
        print "touched"
        self.idm = binascii.hexlify(tag.idm)
        # LED
        GPIO.output(22,1)   #BlueLEDon
        time.sleep(0.5)
        GPIO.output(22,0)
        return True

    def read_id(self):
        clf = nfc.ContactlessFrontend('usb')
        try:
            clf.connect(rdwr={'on-connect': self.on_connect})
        finally:
            clf.close()

def main(ids_csv_filename):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17,GPIO.OUT) #Red
    GPIO.setup(27,GPIO.OUT) #Green
    GPIO.setup(22,GPIO.OUT) #Blue
    GPIO.output(17,0)       #LEDoff
    GPIO.output(27,0)
    GPIO.output(22,0)
    print "Started idm_reader !!!"
    cr = MyCardReader()
    while True:
#        print "touch card:"
        cr.read_id()
#        print "released"
#        print cr.idm

        with open(ids_csv_filename, 'a') as ids_csv_file:   #csv open
            print "Successfully get IDm."
            print "IDm: " + cr.idm

            now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            ids_csv_file.write("{},{}\n".format(now, cr.idm))
            ids_csv_file.close()

            idm_dec =int(cr.idm,16)
            if idm_dec == finIDm:
                break

    print "Stopped idm_reader"


if __name__ == '__main__':
    main(sys.argv[1])
