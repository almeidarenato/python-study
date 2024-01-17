#loop while - enquanto
contador = 0

# contagem até 4
while contador < 5:
    print("Contagem",contador)
    contador += 1

# break força a saida do loop
contador = 0
while contador < 5:
    contador+=1
    if contador == 4:
        break
print(contador)