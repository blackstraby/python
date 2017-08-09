'''
@@Author: Black Straby
@@Date: 02 jan 2017
@@Script: consulta_cotacao.py
@@Version: 0.0.2
@@Description: Atraves da API do site promasters.net.br, monitora cotacao do Euro, Dolar e Bitcoin a cada 5s.
Basta um CTRL+C para finalizar o programa.
'''

import requests
import json
import time
import datetime
import os

while True:

	try:
		req = requests.get('http://api.promasters.net.br/cotacao/v1/valores')
		cotacao = json.loads(req.text)

		if os.name == "nt":
			os.system("cls")
		else:
			os.system("clear")

		print("#### COTACAO ####  ", datetime.datetime.now())
		print("Cotacao do Dolar atual:", cotacao['valores']['USD']['valor'])
		print("Cotacao do Euro atual:", cotacao['valores']['EUR']['valor'])
		print("Cotacao do BitCoin atual:", cotacao['valores']['BTC']['valor'])

		time.sleep(5)

	except KeyboardInterrupt:
		print("Fechando cotacaos...")
		time.sleep(1)
		exit()

	except Exception as e:
		print("Something went wrong :S", e)
		exit()
