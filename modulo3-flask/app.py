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