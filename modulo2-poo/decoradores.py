# Decoradores
# Adicionamos funcionalidades sem alterar o código da própria função.
# Exemplo : Adicionar uma autorização

def meu_decorador(func):
    def wrapper():
        print("Antes da função ser chamada")
        func()
        print("Depois da função ser chamada")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Minha funçao foi chamada")

minha_funcao()

# Abordagem menos comum. Porém muitas bibliotecas utilizam.

class MeuDecoradorDeClasse:
    def __init__(self,func) -> None:
        self.func = func 

    def __call__(self) -> any:
        print("Antes da função ser chamada")
        self.func()
        print("Depois da função ser chamada")

@MeuDecoradorDeClasse
def segunda_funcao():
    print("Segunda funçao foi chamada")

segunda_funcao()