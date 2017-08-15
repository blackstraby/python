import bs4
import requests


def btc():
    site = "https://br.investing.com/currencies/btc-brl"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    result = requests.get(site, headers=headers)

    soup = bs4.BeautifulSoup(result.content.decode(), "html.parser")

    valorBTC = soup.find(id="last_last").text
    valorBTC = valorBTC.replace('.', '')
    valorBTC = valorBTC.replace(',', '.')

    return float(valorBTC[0:5])

maxima = btc()
baixa = btc()

while True:
    try:
        cotacao = btc()

        if cotacao > maxima:
            print("Cotacao maxima anterior:", maxima)
            maxima = cotacao
            print("Bitcoin subindo R$", maxima)

        if cotacao < baixa:
            print("Cotacao baixa anterior:", baixa)
            baixa = cotacao
            print("Bitcoin descendo R$", baixa)

    except Exception as e:
        print(e)
