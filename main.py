# sudo pip3 install beautifulsoup4
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
import requests


def get(url):
    data = requests.get(url)
    # data_clean = data.content.decode("UTF-8")

    parsed_html = BeautifulSoup(data.content, 'html.parser')
    result = parsed_html.body.find('div', attrs={'class':"m-ok"}).text
    print(result)
    return result

# alias per="python3 ~/permesso-di-soggiorno/main.py"
url = 'https://questure.poliziadistato.it/stranieri/?mime=1&lang=english&pratica=xxxxx(Permesso code)'
get(url)

