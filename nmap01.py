#!/usr/bin/python3
import socket
ip=input("Enter IP: ")
port=input("Enter port: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)
if sock.connect_ex((ip,int(port))):
        print("port ", port, "is closed or operation timed out.")
else:
        print("port", port,  "is open.")