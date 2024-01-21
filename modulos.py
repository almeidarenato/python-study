# Modulos - arquivos que podem ser reutilizados em outros programas/arquivos
# Já existem modulos no python. E há modulos de terceiros

print("Exemplo de importação de módulo padrão:")
# Dessa forma importamos todo o módulo
## import math 
# Dessa forma importamos só o código que queremos
from math import sqrt

raiz_quadrada =  sqrt(25)
print("Raiz quadrada de 25 é ",raiz_quadrada)

# O Ideal é importar apenas oque precisa ser usado

# Como criar seu próprio módulo e como usa-lo
print("\n Exemplo de criação e utilização de um módulo personalizado")
from meu_modulo import saudacao,dobro

mensagem = saudacao("Renato")
print(mensagem)
dobro = dobro(4)
print("Dobro de 4 é", dobro)