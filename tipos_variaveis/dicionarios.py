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