#!C:\Python27

# Import our required libraries
import os
import re
import socket
import time

network = '10.250.250.250'
port = 6667

while 1:

	ids_to_trigger = [1116]
	for id in ids_to_trigger:
		os.system('wevtutil qe System "/q:*[System [(EventID=' + str(id) +')]]" /f:text > mselog.txt' )

	os.system('ipconfig > ipconfig.txt')

	file1 = open('ipconfig.txt','r')
	file2 = open('ip.txt', 'w')

	for line in file1:
		if re.search('IPv4 Address', line):
			line = line.split(" ")[16]
			file2.write(line)

	filesize = os.lstat("mselog.txt")[6]

	file1.close()
	file2.close()

	if filesize == 0:
		time.sleep(1)
	else:
		file3 = open('ip.txt', 'r')
		for row in file3:
			line = line.replace('\n','')
			irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
			irc.connect ( ( network, port ) )
			irc.send ( 'NICK mse1\r\n' )
			data = irc.recv ( 4096 )
			data = data.split(":")[1]
			irc.send ( 'PONG ' + data + '\r\n' )
			irc.send ( 'USER mse1 completely real :Jxxx\r\n' )
			irc.send ( 'JOIN #arttreport\r\n' )
			irc.send ( 'PRIVMSG #arttreport :Investigate ' + row + ' on me!\r\n' )
			irc.send ( 'QUIT :Testing message\r\n' )
			irc.close()

		file3.close()
	os.system('del ipconfig.txt')
	os.system('del mselog.txt')
	os.system('del ip.txt')
	os.system('wevtutil CL System')
	time.sleep(300)
