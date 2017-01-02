#!/bin/bash
		##############################################
		#	@@Author: Black Straby				          	 #
		#   @@Date: June 13th, 2016 				         #
		#	@@Function: Extrair usuarios do sistema	   #
		##############################################

usr=( $(cut -d: -f1 /etc/passwd) )

echo "Total de usuarios no sistema:"
echo ${usr[*]}
echo ''

echo "UID dos Usuarios no sistema:"
echo  ${!usr[*]}
echo ''
