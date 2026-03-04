import requests
from bs4 import BeautifulSoup

url = "https://pomofocus.io/"
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

contar_titulos = 0
contar_paragrafos = 0

for linha_texto in extracao.find_all('h1'):
    tag_h1 =linha_texto.find('h1')
    titulo =tag_h1.text
    contar_titulos += 1
    print(titulo)

