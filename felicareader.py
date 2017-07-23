# -*- coding: utf-8 -*-
'''
###
'''

import binascii
import datetime
import sys
import time
import socket

import nfc
from RPi import GPIO

HOST = '---'
PORT = ---
INTERVAL = 3
RETRYTIMES = 5

finIDm = 77408918205372968  #0113030040141A28
RasNum = 1

def socket_connect(host, port, interval, retries):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for x in range(retries):
        try:
            sock.connect((host, port))
            return sock
        except socket.error:
            print "Wait"+str(interval)+"sec"
            time.sleep(interval)

    sock.close()
    return None

def main(ids_csv_filename):
    with open(ids_csv_filename, 'a') as ids_csv_file:
        clf = nfc.ContactlessFrontend('usb')

        sock = socket_connect(HOST, PORT, INTERVAL, RETRYTIMES)

        if sock is None:
            print "system exit:connection error"
            sys.exit(0)

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

            sock.send(idm,RasNum)

            now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            ids_csv_file.write("{},{}\n".format(now, idm))

            idm_dec = int(idm,16)
            if idm_dec ==  finIDm:
                sock.send("quit")
                sock.close()
                break

        GPIO.cleanup()
        print "Stopped FeliCaReader."

if __name__ == '__main__':
    main(sys.argv[1])
