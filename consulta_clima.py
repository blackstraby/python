'''
@@Author: Black Straby
@@Date: 02 jan 2017
@@Script: consulta_clima.py
@@Description: Atraves da API do site openweathermap.org, retorna o estado do tempo na cidade indicada e a temperatura.
''' 

import requests
import json

def tempo_atual(cidade):
	req = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=SUA-KEY-AQUI')
	tempo = json.loads(req.text)
	return tempo


def celsius(temp):
	celsius = 0
	celsius = float(temp) - 273.15
	return "{0:.2f}".format(celsius)

cidade = input("Digite sua cidade: ")

lista = tempo_atual(cidade)
temperatura = float(lista['main']['temp'])

print('Condicao:', lista['weather'][0]['main'])
print('Temperatura:', celsius(temperatura),'C')
