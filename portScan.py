#!/usr/bin/python3
# -*- coding: utf-8 -*-

from socket import *
import sys
import getopt

def usage():
        print ("			Strabear PortScan ")
        print ('			@@Version: 1.0')
        print ('			@@Created by Black Straby')
        print ('			@@Date: 7 jan 2017')
        print ('')
        print ("Usage: ./portScan.py alvo")
        print ('-t	--target 	= Alvo')
        print ('-p 	--port		= Porta (O script executura da porta 1 a porta passada)')
        print ('-v 	 --version 	= Mostra a versão e encerra')
        print ('-h	 --help		= Menu de ajuda')
        print ('')
        print ("Examples: ")
        print ("portScan.py  -h www.google.com 	-p 22")
        print ("portScan.py  -h 192.168.0.104 	-p 65536")
        print ('')
        sys.exit(0)

def scan_host(host, port, r_code = 1):
	try:
		s = socket(AF_INET, SOCK_STREAM)
		code = s.connect_ex((host, port))

		if code == 0:
			r_code = code
		s.close()

	except Exception as e:
		pass

	return r_code


def main():
	if not len(sys.argv[1:]):
		usage()
	try:
	    opts, args = getopt.getopt(sys.argv[1:], 't:p:h:v', ['target=', 'port=','version','help'])
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	try:
		for opt, arg in opts:
			if opt in ('-h', '--help'):
				usage()
				sys.exit(2)
			elif opt in ('-t', '--target'):
				host = arg
			elif opt in ('-p', '--port'):
				port = int(arg)
			elif opt in ('-v', '--version'):
				print('Versao atual: 1.0')
				exit()
			else:
		   		usage()
		   		sys.exit(2)

	except KeyboardInterrupt:
		print("\n\n\033[31m[*] Cancelado pelo Usuário.033[0;0m")
		print("\n\n[*] Finalizando programa..")
		sys.exit(1)

	hostip = gethostbyname(host)
	if host == hostip:
		print("\n[+] IP: %s " % (hostip))	
	else:
		print("\n[+] Host: %s IP: %s" % (host, hostip))

	for port in range(port+1):
		try:
			resposta = scan_host(host, port)

			if resposta == 0:
				print("[+] Port %d: Open" % (port))
		except Exception as e:
			print(e)

	print("[+] Scanning completo com sucesso.")

main()
