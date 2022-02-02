#!/usr/bin/python3

import socket as sck
import OpenApps_mac.opening_apps as open_app 

if __name__ == "__main__":
	# Opening Google Chrome
    open_app.launch_app("Google Chrome")
    # Connecting to native program
    s = sck.socket(family=sck.AF_INET, type=sck.SOCK_STREAM)
    s.bind(('localhost', 50000))
    s.listen()
    connection, address = s.accept()
    message = input(">> ")
    
    # Tab list: {tabId: URL}
    tabs = {}

    # Looping over user input until quit
    while len(message) > 0:
        if message.split(",")[0] == "open":
            connection.sendall(message.encode())
            data = connection.recv(1024)     # 1024 max bytes
            tabs[data.decode()] = message.split(",")[1]
        elif message.split(",")[0] == "close":
            connection.sendall(message.encode())
            data = connection.recv(1024)
            del tabs[message.split(",")[1]]
        elif message.split(",")[0] == "switch":
            connection.sendall(message.encode())
            data = connection.recv(1024)
            print(data.decode())
        if message == "quit":
            open_app.close_app("Google Chrome")
            break
        print(tabs)
        message = input(">> ")
    connection.close()

