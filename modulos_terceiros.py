# Para instalar pacotes terceiros é necessário usar
# o gerenciador de pacotes PIP
# para instalar a biblioteca request use:
# pip install requests ou pip3 install requests 
# também é possível instalar uma versao especifica com:
# pip3 install requests==2.31.0
print("\n Fazendo a importação e uso de um módulo de terceiros")
import requests 

url = "https://www.rocketseat.com.br/"
response = requests.get(url)
print("Status de Retorno",response.status_code)