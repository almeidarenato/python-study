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

# otimização 
    
    #range(): intervalo numérico 
    # [0,1,2,3,4,5,6,7,8,9]
print(list(range(0,10)))

for numero in range(5):
    print("numero",numero)

# utilizando a função range() com len() para percorrer listas
lista = [1,2,3,4,5]
for indice in range(0,len(lista)):
    print(lista[indice])
    if(lista[indice] ==3 ):
     lista[indice] =0
print(lista)

#enumerate() retorna a lista com o indice e o valor
lista_enumerate = ["a","b","c"]
for indice,elemento in enumerate(lista_enumerate):
    print(f"{indice},{elemento}")

print(enumerate(lista_enumerate))