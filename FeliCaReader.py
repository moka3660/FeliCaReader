# -*- coding: utf-8 -*-
'''
This script is for ...

'''

import binascii
import datetime
import sys
import time

import nfc
from RPi import GPIO

class DoorManager(object):
    _PIN_OPEN = 27
    _PIN_CLOSE = 17

    @property
    def is_locked(self):
        return self._is_locked

    def __enter__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._PIN_OPEN, GPIO.OUT)
        GPIO.setup(self._PIN_CLOSE, GPIO.OUT)
        self._is_locked = False
        print "Started door control."
        return self

    def __exit__(self, type, value, traceback):
        GPIO.cleanup()
        print "Stopped door control."

    def lock(self):
        if self._is_locked:
            print "Already locked."
            return

        GPIO.output(self._PIN_CLOSE, True)
        time.sleep(0.5)
        GPIO.output(self._PIN_CLOSE, False)
        self._is_locked = True
        print "Sucessfully locked."

    def unlock(self):
        if not self._is_locked:
            print "Already unlocked."
            return

        GPIO.output(self._PIN_OPEN, True)
        time.sleep(0.5)
        GPIO.output(self._PIN_OPEN, False)
        self._is_locked = False
        print "Sucessfully unlocked."


def main(registered_ids_csv_filename, log_csv_filename):
    with open(registered_ids_csv_filename) as registered_ids_csv_file:
        registered_ids = [l.rstrip().split(',') for l in registered_ids_csv_file]

    if not registered_ids:
        print "No one is registered."
        return
    name_by_id = {t[0]: t[1] for t in registered_ids}

    with open(log_csv_filename, 'a') as log_csv_file, DoorManager() as door_manager:
        clf = nfc.ContactlessFrontend('usb')
        print "Press ^C to quit ..."
        while True:
            time.sleep(1.0)

            tag = clf.connect(rdwr={'on-connect': None})
            if not isinstance(tag, nfc.tag.tt3.Type3Tag):
                print "Invalid card type."
                continue
            idm = binascii.hexlify(tag.idm)

            if idm not in name_by_id:
                print "Invalid ID: {}".format(idm)
                continue
            name = name_by_id[idm]

            if door_manager.is_locked:
                print "Welcome, {} ({})!".format(name, idm)
                door_manager.unlock()
            else:
                print "Goodbye, {} ({})!".format(name, idm)
                door_manager.lock()

            # logging
            now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    #        action = "closed" if door_manager.is_locked else "opened"
            log = "{},{},{},{}\n".format(now, idm, name)
            log_csv_file.write(log)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
