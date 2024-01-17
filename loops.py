# loops em python - repetição de código e automatizar tarefas repetidas

lista = [1,2,3,4,5]

# para variavel in sequencia de elementos
# pra cada elemento é feito um print diferente 
for elemento in lista:
    print(elemento)

tupla = (1,2,3,4,5)

for elemento in tupla:
    print(elemento)

pessoa = {"nome": "Joao", "idade": 30 , "cidade": "São Paulo"}
print("\nFor Dicionario - chaves")

for chave in pessoa.keys():
    print(chave)

print("\nFor Dicionario - valores")

for valor in pessoa.values():
    print(valor)

print("\nFor Dicionario ")

for chave,valor in pessoa.items():
    print(f"{chave}:{valor}")