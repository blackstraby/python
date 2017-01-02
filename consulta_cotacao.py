'''
@@Author: Black Straby
@@Date: 02 jan 2017
@@Script: consulta_cotacao.py
@@Description: Atraves da API do site promasters.net.br, monitora cotacao do Euro, Dolar e Bitcoin a cada 5s. Basta um CTRL+C para finalizar o programa.
''' 

import requests
import json
import time
import datetime
import os

while True:

	try:
		if os.name == "nt":
			os.system("cls")
		else:
			os.system("clear")

		req = requests.get('http://api.promasters.net.br/cotacao/v1/valores')
		cotacao = json.loads(req.text)

		print("#### COTACAO ####  ", datetime.datetime.now())
		print("Cotacao do Dolar atual:", cotacao['valores']['USD']['valor'])
		print("Cotacao do Euro atual:", cotacao['valores']['EUR']['valor'])
		print("Cotacao do BitCoin atual:", cotacao['valores']['BTC']['valor'])

		time.sleep(5)

	except KeyboardInterrupt:
		print("Fechando cotacaos...")
		time.sleep(2)
		exit()

	except Exception as e:
		print("Something went wrog :S", e)
		exit()
