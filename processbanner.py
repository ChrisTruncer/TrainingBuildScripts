#!C:\Python27

# Import our required libraries
import os
import re
import socket
import time

network = '10.250.250.250'
port = 6667

while 1:
	# Use the OS command to dump running processes minus those which are whitelisted within the command
	os.system('tasklist /fi \"IMAGENAME ne System Idle Process\" /fi \"IMAGENAME ne System\" /fi \"IMAGENAME ne tasklist.exe\" /fi \"IMAGENAME ne dwm.exe\" /fi \"IMAGENAME ne explorer.exe\" /fi \"IMAGENAME ne svchost.exe\" /fi \"IMAGENAME ne dfssvc.exe\" /fi \"IMAGENAME ne vmtoolsd.exe\" /fi \"IMAGENAME ne smss.exe\" /fi \"IMAGENAME ne crss.exe\" /fi \"IMAGENAME ne winint.exe\" /fi \"IMAGENAME ne services.exe\" /fi \"IMAGENAME ne lsass.exe\" /fi \"IMAGENAME ne lsm.exe\" /fi \"IMAGENAME ne MsMpEng.exe\" /fi \"IMAGENAME ne SLsvc.exe\" /fi \"IMAGENAME ne spoolsv.exe\" /fi \"IMAGENAME ne dfsrs.exe\" /fi \"IMAGENAME ne dns.exe\" /fi \"IMAGENAME ne ismserv.exe\" /fi \"IMAGENAME ne processbanner.exe\" /fi \"IMAGENAME ne dfssvc.exe\" /fi \"IMAGENAME ne dllhost.exe\" /fi \"IMAGENAME ne msdtc.exe\" /fi \"IMAGENAME ne csrss.exe\" /fi \"IMAGENAME ne winlogon.exe\" /fi \"IMAGENAME ne taskeng.exe\" /fi \"IMAGENAME ne dwm.exe\" /fi \"IMAGENAME ne explorer.exe\" /fi \"IMAGENAME ne msseces.exe\" /fi \"IMAGENAME ne Oobe.exe\" /fi \"IMAGENAME ne mmc.exe\" /fi \"IMAGENAME ne taskmgr.exe\" /fi \"IMAGENAME ne cmd.exe\" /fi \"IMAGENAME ne TrustedInstaller.exe\" /fi \"IMAGENAME ne WmiPrvSE.exe\" /fi \"IMAGENAME ne wininit.exe\" /fi \"IMAGENAME ne logbanner.exe\" /fi \"IMAGENAME ne MSEdetector.exe\" /fi \"IMAGENAME ne MSASCui.exe\" /fi \"IMAGENAME ne wuauclt.exe\" /fi \"IMAGENAME ne SLUI.exe\" > processes.txt')

	# Open our files we will be reading from and writing to
	file = open('processes.txt','r')
	file2 = open('badprocesses.txt','w')

	# Loop that "greps" for the IP address and writes it to a file
	for line in file:
		line = line.split(" ")[0]
		file2.write(line + '\n')

	file.close()
	file2.close()
	file3 = open('badprocesses.txt','r')
	processes = file3.readlines()
	file4 = open('sanitizedprocess.txt','w')
	file4.writelines(processes[4:])

	file3.close()
	file4.close()

	os.system('del processes.txt')
	os.system('del badprocesses.txt')

	filesize = os.lstat("sanitizedprocess.txt")[6]

	if filesize == 0:
		time.sleep(1)
	else:
		targetfile = open('sanitizedprocess.txt','r')
		sortedprocesses = targetfile.readlines()
		targetfile.close()
		for process in sortedprocesses:
			process = process.strip()
			irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
			irc.connect ( ( network, port ) )
			irc.send ( 'NICK pban1\r\n' )
			data = irc.recv ( 4096 )
			data = data.split(":")[1]
			irc.send ( 'PONG ' + data + '\r\n' )
			irc.send ( 'USER pban1 completely real :Jxxx\r\n' )
			irc.send ( 'JOIN #arttreport\r\n' )
			irc.send ( 'PRIVMSG #arttreport :Investigate ' + process + ' on me!\r\n' )
			irc.send ( 'QUIT :Testing message\r\n' )
			irc.close()

	os.system('del sanitizedprocess.txt')
	time.sleep(300)
