from __future__ import print_function
import socket
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)
from contextlib import closing

def main():

  while True:
    inputValue = GPIO.input(25)
    if (inputValue == True):
      send()
    time.sleep(1)

def send(): #送信処理

  host = '192.168.1.0' #送信先IP
  port = 8080 '送信先Port
  bufsize = 4096

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(0.5) #接続タイムアウト値設定

  with closing(sock):
    try:
      sock.connect((host, port))
      sock.send(b'raspberry')
    except socket.timeout:
      print(b'socketTimeout')
    except socket.error:
      print(b'socketError')
    time.sleep(5)
  return

if __name__ == '__main__':
  main()
