#!/bin/bash
		#########################################
		#	@@Author: Black Straby      	#
		#	@@Date: 02 jan 2017		#
		#   SCRIPT DE FIREWALL - IPTABLES  	#
		#########################################

if [ $USER != 'root' ];then
	echo "Voce precisa estar como Usuario Administrativo!"
	exit
else

	echo "Exemplo: 192.168.0.1/255.255.255.0 ou 10.0.0.1/255.255.255.0"
	echo ''
	echo -n "Digite seu range de IP: "
	read ip

	echo -n "Digite sua interface de rede (eth0, wlan0...): "
	read interface

	# Abrir para uma faixa de enderecos
	iptables -A INPUT -s $ip -i $interface -j ACCEPT


	# Fechando Portas - rpcbind e smtp e mysql
	echo -e '\033[01;32m[+] Fechando portas 25, 111 e 3306 \033[00;37m'
	sleep 1
	iptables -A INPUT -p tcp --destination-port 111 -j DROP
	iptables -A INPUT -p tcp --destination-port 25 -j DROP
	iptables -A INPUT -p tcp --destination-port 3306 -j DROP


	# Abrir portas 22, 80 e 443
	echo -e '\033[01;32m[+] Permitindo portas 22, 80 e 443 \033[00;37m'
	sleep 1
	iptables -A INPUT -m multiport -p tcp --dport 22,80,443 -j ACCEPT

	# Abrir intervalo de portas Torrent
	echo -e '\033[01;32m[+] Permitindo intervalo de portas Torrent \033[00;37m'
	sleep 1
	iptables -A INPUT -p tcp --dport 6881:6889 -j ACCEPT

	echo -e '\033[01;35m[+]Concluido. \n \033[00;37m'
	iptables -L
# Verificar alem do IP o MAC address (ex: meu mac)
# iptables -A INPUT -s 192.168.0.101 -m mac --mac-source 90:f6:52:ed:de:14 -j ACCEPT

fi
