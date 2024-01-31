# Flask
# Framework Python para construção de APIs
# Conhecido pela sua simplicidade e facilidade . 
# Escalável e Flexível 
# Um dos Principais frameworks do Python
# Pinterest, LinkedIn , Netflix e Uber utilizam o Flask
# Para instalar pip3 install Flask 
# Para instalar uma versão específica podemos usar pip3 install Flask==2.3.0 (exemplo)
# O arquivo requirements.txt no python serve para listar as dependencias
# Para instalar os modulos a partir do arquivo de Dependências basta usar 
# pip3 install -r requirements.txt

# Protocolo HTTP:
# Métodos GET , POST , PUT , DELETE , PATCH
# GET - Solicita a Representação de um recurso específico (endpoint). Deve retornar apenas dados.
# POST - O método POST é utilizado para submeter uma entidade/informações a um recurso específico. Causando uma mudança no estado do recurso ou efeitos colaterais no servidor.
# PUT - Substitui todas as informações de uma entidade/recurso específico. Portanto você é obrigado a substituir tudo.
# PATCH -  Aplica modificações parciais
# DELETE - Remove um recurso específico.


# Rest (Representational State Transfer) Obrigatoriamente usamos JSON e XML para representar
# Api Rest x Api Restful
# Api Rest = estilo de arquitetura para desenvolvimento de API
# Rest princípios/regras que vão permear as comunicações entre os sistemas
# Quando a API respeita todos os padrões de Rest , são Restful

# Códigos de Resposta / Response
# (100 a 199) - Respostas Informativas
# (200 a 299) - Respostas bem sucedidaes
# (300 a 399) - Mensagens de redirecionamento
# (400 a 499) - Respostas de erro do cliente
# (500 a 599) - Respostas de erro do servidor

from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello World"

@app.route("/about")
def about():
    return "Página sobre"
# se __name__ = __main__ significa que o servidor está sendo executado manualmente
if __name__ == "__main__":
    app.run(debug=True)