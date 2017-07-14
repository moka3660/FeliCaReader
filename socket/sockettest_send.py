#import binascii
import datetime
import sys
import time
import socket

#HOST = '153.126.194.52' #送信先IP
#PORT = 8001 #送信先ポート
#INTERBAL = 3 #リトライ間隔[sec]
#RETRYTIMES = 5 #リトライ回数

def send(): #送信処理

  host = '153.126.194.52' #送信先IP
  port = 8001 '送信先Port
#  bufsize = 4096

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


def main(): #実行時に一度テキスト送信のみ

    send()

if __name__ == '__main__':
    main()
