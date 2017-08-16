import bs4
import requests
import ChavesAPI
from datetime import datetime


def btc():
    site = "https://br.investing.com/currencies/btc-brl"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/50.0.2661.102 Safari/537.36'}
    result = requests.get(site, headers=headers)

    soup = bs4.BeautifulSoup(result.content.decode(), "html.parser")

    valorBTC = soup.find(id="last_last").text
    valorBTC = valorBTC.replace('.', '')
    valorBTC = valorBTC.replace(',', '.')

    return float(valorBTC[0:5])


def main(alta, baixa):
    while True:
        try:
            cotacao = btc()

            if cotacao > (alta + 500):
                print("Cotacao maxima anterior:", alta)
                alta = cotacao
                print("Bitcoin subindo R$", alta)

                ChavesAPI.twitter1.notify("Cotacao aumentou as " + data + " ")

            if cotacao < (baixa - 500):
                print("Cotacao baixa anterior:", baixa)
                baixa = cotacao
                print("Bitcoin descendo R$", baixa)

                ChavesAPI.twitter1.notify("Cotacao diminuiu as " + data + " ")

        except Exception as e:
            print(e)

agora = datetime.now()
data = str(agora.day) + "/" + str(agora.month) + " - " + str(agora.hour) + ":" + str(agora.minute)

maxima = btc()
minima = btc()

main(maxima, minima)
