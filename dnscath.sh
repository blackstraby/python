#!/bin/bash
		#################################################
		#	    @@Author: Black Straby			              #
		#   	@@Date: June 13th, 2016 		              #
		#	    @@Function: Extrair informacoes por DNS	  #
		#################################################

figlet DNSCATCH

echo -e '\033[01;31m[+] Sintaxe ./dnscatch alvo.com \033[01;32mwordlist.txt \033[00;37m'
echo -n "Executar? (S/n)"
read resp

if [ $1 -z ];then
		echo 'Voce nao passou alvo.com como parametro.'
		exit
elif [ $2 -z ];then
		echo 'Voce nao passou uma wordlist como parametro.'
		exit
else

	if [ $resp == 's' ];then
		{	
			


			echo -e '\033[01;32m[+] Iniciando varredura em zonas e mailserver \033[00;37m'
			sleep 1

			host -t ns $1	 	#argumento 1
			host -t mx $1
			echo -e "\n\n"

			echo -e '\033[01;32m[+] Fazendo Transferencia de Zona...\n\033[00;37m'
			sleep 1
			#Transferencia de zona    delimitador espaço e coluna 4
			for ns in $(host -t ns $1 | cut -d " " -f 4);
			do
				host -l $1 $ns;
			done

			echo -e "\n\n"
			echo -e '\033[01;32m[+] Fazendo BruteForce na wordlist...\n\033[00;37m'

			for palavra in $(cat $2);  #argumento 2 - wordlist
			do
				host $palavra.$1 |grep "has address"
			done
		}
	else
		exit
	fi
fi
