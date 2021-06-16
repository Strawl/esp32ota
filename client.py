from datetime import datetime
import socket
import threading

TCP_DESTINATION_IP = input("Which server would you like to connect to? ")
TCP_DESTINATION_PORT = int(input("What port does this server have? "))
USERNAME = input("What username would you like to have? ")
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_DESTINATION_IP, TCP_DESTINATION_PORT))

print("You may start chatting")


def get_messages():
    while True:
        x = input()
        if not t1.is_alive():
            break
        # x = USERNAME + ": " + x
        s.sendall(x.encode('utf-8'))


def receive_message():
    while True:
        data = s.recv(BUFFER_SIZE)
        data = str(data)[2:-1]
        if data == "kick":
            print("The server has kicked you. Press enter to exit")
            s.close()
            break;
        print(f"{datetime.now().strftime('%d/%m/%Y %H:%M')} {data}")


try:
    t1 = threading.Thread(target=receive_message)
    t1.start()
    get_messages()
except:
    s.close()
s.close()
