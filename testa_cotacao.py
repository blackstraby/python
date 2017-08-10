import time
import requests
import json
import ChavesAPI
from datetime import datetime

agora = datetime.now()
data = str(agora.day) + "/" + str(agora.month) + " - " + str(agora.hour) + ":" + str(agora.minute)


def consultaCotacao(moeda="USD"):
    try:
        req = requests.get('http://api.promasters.net.br/cotacao/v1/valores')
        cotacao = json.loads(req.text)

        return cotacao['valores'][moeda]['valor']

    except Exception as e:
            print("Something went wrong :S", e)


def checkUSD():
    valorDolar = consultaCotacao("USD")

    while True:
        valorAnterior = valorDolar
        valorDolar = consultaCotacao("USD")

        try:
            if valorDolar > valorAnterior:
                ChavesAPI.twitter1.notify("Cotacao aumentou as " + data + " ")

            if valorDolar < valorAnterior:
                ChavesAPI.twitter1.notify("Cotacao diminuiu as " + data + " ")

            else:
                pass

            time.sleep(30)

        except KeyboardInterrupt:
            print("Fechando cotacoes...")
            exit()

        except Exception as e:
            print("Something went wrong :S", e)


def main():
    checkUSD()
    pesquisa = ChavesAPI.twitter2.search()
    for result in pesquisa:
        print(result['text'])
        print(result['user']['screen_name'], '\n')


main()
