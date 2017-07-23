#coding:utf-8
import binascii
import datetime
import sys
import time
import socket
import threading

HOST = '---'
PORT = ---
CLIENTNUM = 3

class ConnClient(threading.Thread):
    def __init__(self, conn, addr):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()
        self.conn_socket = conn
        self.addr = addr

    def run(self):
        try:
            while (1):
#                senddata = raw_input(str(self.addr)+"SendData:")
#                self.conn_socket.send(senddata)
                recvdata = self.conn_socket.recv(1024)
                print "ReciveData"+recvdata+str(self.addr)
                now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                ids_csv_file.write("{},{}\n".format(now, recvdata))
                if (recvdata == "quit"):
                    break

        except socket.error:
            print "connect errer"

        finally:
            self.conn_socket.close()
            print "connect close"

    def stop(self):
        self.conn_socket.cloce()

def main(ids_csv_filename):
    with open(ids_csv_filename, 'a') as ids_csv_file:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((HOST, PORT))
        sock.listen(CLIENTNUM)

        while (1):
            conn, addr = sock.accept()
            print("Connected by"+str(addr))
            connClientThread = ConnClient(conn, addr)
            connClientThread.setDaemon(True)
            connClientThread.start()

if __name__ == '__main__':
    main(sys.argv[1])
