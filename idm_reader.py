# -*- coding: utf-8 -*-

import binascii
import nfc

finIDm = 72340248454488070  #010101129C17E006

class MyCardReader(object):

    def on_connect(self, tag):
        print "touched"
        self.idm = binascii.hexlify(tag.idm)
        return True

    def read_id(self):
        clf = nfc.ContactlessFrontend('usb')
        try:
            clf.connect(rdwr={'on-connect': self.on_connect})
        finally:
            clf.close()

if __name__ == '__main__':
    cr = MyCardReader()
    while True:
        print "touch card:"
        cr.read_id()
        print "released"
        print cr.idm

        idm_dec =int(cr.idm,16)
        if idm_dec == finIDm:
            break
