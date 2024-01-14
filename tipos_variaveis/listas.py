# Lista - coleção de elementos ordenáveis 

# Declaração
minha_lista = [1,2,3,4,5,"texto",True,False,8]

# cada elemento possui um indice
print(f"Minha lista de exemplo {minha_lista}")
#ou
print(f"minha_lista[0]: {minha_lista[0]}")
print(f"minha_lista[5]: {minha_lista[5]}")

# fatiar uma lista , pegar uma parte dela ou slice
print(f"minha_lista[1:6]: {minha_lista[1:6]}")
# também é possível pegar do começo em diante
print(f"minha_lista[:5]: {minha_lista[:5]}")
# do elemento até o fim
print(f"minha_lista[3:]: {minha_lista[3:]}")

minha_lista[0] = "Renato"
print(f"Nova lista {minha_lista}")

#Métodos de lista

# Método append() : Adiciona um elemento ao final da lista
minha_lista.append(6)
print(f"Nova lista após o append {minha_lista}")

#Método index : Retorna o indice do elemento especificado
indice = minha_lista.index("texto")
print(f"Indice do elemento 'texto': {indice}")

#Método insert : Adiciona um item em um índice específico
minha_lista.insert(1,"Novo Elemento")
print(f"Inserido texto novo elemento no indice 1 {minha_lista}")

# Método pop : Retorna e Remove o elemento de um índice específico
print(f"Removido elemento numero 2 com pop {minha_lista.pop(1)}")

#Método remove : Remove elemento especificado no parametro. Se houver mais de um elemento igual ao parametro ele remove começando 
# pelo ultimo na ordem da lista
minha_lista.remove(8)
print(f"Remoção do numero 8 com remove {minha_lista}")

#Método sort: Organiza a lista. Porém a lista precisa ter elementos do mesmo tipo para que funcione
lista_de_numeros = [1,4,8,3,9,0,2,0,1]
lista_de_numeros.sort()
print(f"Lista organizada {lista_de_numeros}")