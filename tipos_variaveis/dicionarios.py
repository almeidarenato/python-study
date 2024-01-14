# tipo dicionario - Dicionário é uma coleção não ordenada, de pares chave: valor
#Elementos de dentro do dicionário também podem ser um dicionário
#Criando um dicionário de exemplo
pessoa = {"nome": "Renato","idade": 30, "cidade":"São Paulo"}
print(f"{pessoa}")
#Acessando valores
print(f"{pessoa["nome"]}")
print(f"{pessoa["idade"]}")
print(f"{pessoa["cidade"]}")

#Atribuir novos valores
pessoa["sobrenome"] = "Almeida"
print(f"{pessoa["sobrenome"]}")

#Atualizar um valor existente
pessoa["idade"] = 31
print(f"{pessoa["idade"]}")

#remover um par de chave e valor
del pessoa["sobrenome"]
print(f"{pessoa}")

#Métodos : keys() , values() - lista dos valores , items() - lista de tuplas de pares de chave e valor
chaves = pessoa.keys()
print("Chaves do dicionario",chaves)
#para que o elemento retornado se torne uma lista é possível fazer a conversão (ou cast) dessa forma
chaves = list(pessoa.keys())
print("Chaves do dicionario",chaves)
valores = pessoa.values()
print("Valores do dicionario",valores)

items = pessoa.items()
print("Items do dicionario",items)
#para acessar o par desta tupla é necessário fazer da seguinte forma:
items = list(pessoa.items())
print(f"Primeira chave e valor: {items[0][0]} = {items[0][1]}")

