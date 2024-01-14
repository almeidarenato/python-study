""" tupla é uma coleção (lista) ordenada e imutável de elementos . Portanto depois de declarada ela é estática,
 não se pode remover ou incluir elementos"""

#Criando uma tupla - utiliza-se () ao invés de []
minha_tupla = (1,2,2,3,4)
print(f"{minha_tupla}")

print(f"{minha_tupla[3]}")
print(f"{minha_tupla[:4]}")
print(f"Ultimo elemento {minha_tupla[-1]}")

#método count - conta  a quantidade de vezes o parametro informado aparece

contagem = minha_tupla.count(2) 
print(f"Quantidade de vezes o n 2 aparece {contagem}")

#index - exibe o indice do elemento informado
print(f"Indice do elemento 3 : {minha_tupla.index(3)}")