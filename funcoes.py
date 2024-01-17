# Funções

def saudacao(nome):
    print(f"Olá {nome}")

saudacao("Renato")
saudacao("Ana")

## Função com retorno
def ao_quadrado(numero):
    resultado = numero **2
    return resultado

print(ao_quadrado(5))

# Função com multiplos parametros
def soma(numero1,numero2):
    resultado = numero1 + numero2
    return resultado
print("Soma de 300 e 800 é", soma(300,800)) 