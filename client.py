from datetime import datetime
import socket
import threading

TCP_DESTINATION_IP = input("Which server would you like to connect to? ")
TCP_DESTINATION_PORT = int(input("What port does this server have? "))
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_DESTINATION_IP, TCP_DESTINATION_PORT))

print("You may start programming")


def get_messages():
    while True:
        x = input()
        s.sendall(x.encode('utf-8'))


get_messages()
