#!/usr/bin/python3

import json
import sys
import struct
import os
import socket as sck

def get_message():
    """
    stdin message.
    """
    legnth = sys.stdin.buffer.read(4)
    if not length:
        sys.exit(0)
    message_len = struct.unpack('=I', length)[0]
    message = sys.stdin.buffer.read(message_len).decode("utf-8")
    return json.loads(message)

def encode_message(content):
    """
    Encode the message, content.
    """
    encoded_content = json.dumps(content).encode("utf-8")
    encoded_len = struct.pack('=I', len(encoded_content))
    return {'length': encoded_len, 'content': struct.pack(str(len(encoded_content))+"s",encoded_content)}

def send_message(encoded_message):
    """
    stdout message
    """
    sys.stdout.buffer.write(encoded_message['length'])
    sys.stdout.buffer.write(encoded_message['content'])
    sys.stdout.buffer.flush()

message = get_message()

# Setting up socket conn to main program
s = sck.socket(family=sck.AF_INET, type=sck.SOCK_STREAM)
s.connect(('localhost', 50000))

while True:
	retrn = None
	data = s.recv(1024)
	# If main program (server) sends 'quit',
	# 	disconnect client
	if "quit" in data.decode():
		s.close()
		break
	send_message(encode_message(data.decode()))
	retrn = get_message()
	s.sendall(retrn.encode())

