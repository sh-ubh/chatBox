import socket 
import threading

friend_ip="192.168.43.236"
friend_port=4444
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((friend_ip, friend_port))

def send_func():
	while True:
		send = input()
		connection.send(str.encode(send))
def rec_func():
	while True:
		received_data = connection.recv(1024)
		print(str(received_data))

thread1 = threading.Thread(target = send_func)
thread1.start()

thread2 = threading.Thread(target = rec_func)
thread2.start()

connection.close()
