import socket
import time
import threading.threading as threading
import network
import usocket
import gc

#wlan
ssid = "UPC9890593"
pw = "jTrtyu2kj2Hb"

#connect to Wifi
print("Connection to Wifi")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid,pw)

while not wifi.isconnected():
    pass
print("connected")
print("ESP32 online: ", ssid, "IP: ", wifi.ifconfig())


TCP_RECEIVING_IP = input("On what Ip Address should the Server exist? ") or "127.0.0.1"
TCP_RECEIVING_PORT = int(input("On what Port should the Server exist? "))

BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_RECEIVING_IP, TCP_RECEIVING_PORT))

gc.collect()

print("Sockets have been created")

connection_list = []

def attach_clients():
    while True:
        try:
            print("awaiting clients")
            s.listen(1)
            conn, add = s.accept()
            print(conn)
            print(add)
            conn.setblocking(0)
            connection_list.append([conn,add])
        except:
            pass
        
def get_data():
    print("starting get_data loop")
    while True:
        for client in connection_list:
            try:
                data = client[0].recv(BUFFER_SIZE)
                print(data.decode('utf-8'))
                exec(data)
            except:
                pass
            
print("Starting the threads")
t1 = threading.Thread(target=attach_clients)
t1.start()
time.sleep(1)
get_data()
