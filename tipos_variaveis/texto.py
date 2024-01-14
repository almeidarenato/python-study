# Declaração de textos . Recomendaçao do padrão é utilizar " " duplas 
nome_completo = "Renato Almeida"

# Declaração de texto que permite pular linhas
nome_completo_aspas = """Renato
Almeida """

nome_completo_quebra = " Renato \
    Almeida"

nome = "Renato"
sobrenome = "Almeida"

# Formatação de string (adicionar variaveis dentro de uma string)

# com virgula = possui espaço entre a string e variavel
print("Nome Completo(1a forma):",nome_completo)
# com o sinal + = não possui espaço
print("Nome Completo(2a forma):"+nome_completo)

# somando multiplas strings e mesclando com ,
print("Nome Completo(3a forma):"+ "Renato" + "Almeida")
print("Nome Completo(4a forma):"+ "Renato" , "Almeida")
print("Nome Completo(5a forma):", nome_completo_aspas) #com quebra de linha
print("Nome Completo(6a forma):", nome_completo_quebra)
print("Nome Completo(7a forma): [[%s]]"% nome_completo) #com substituição
print("Nome Completo(8a forma): [[%s]]  [[%s]]"% (nome,sobrenome) ) #com substituição e multiplas variáveis , 
print(f"Nome Completo(9a forma): {nome} {sobrenome}") #se chama "format". Precisa do "f" na frente
print("Nome Completo(9a forma): {} {}".format(nome,sobrenome)) #similar ao de cima mas nao usa o "f" na frente


# Métodos especificos para string
#Importante = nenhuma funçao altera o valor da variável. 


#upper() = caixa alta
print(f"Caixa alta : {nome_completo.upper()}")

#lower() = caixa baixa
print(f"Caixa baixa : {nome_completo.lower()}")

#primeira letra - ou qualquer letra bastando alterar o valor em chaves [0]
print(f"letra: {nome_completo[0]}")

#count(parametro) - parametro letra que voce deseja contar dentro da string (not case sensitive)
print(f"Contagem de letra a {nome_completo.count("a")}") 

#find(parametro) - encontra posição da letra (informada no parametro) , iniciando em 0
print(f"Posição da letra a { nome_completo.find("a")}")

#enconde() - codifica variável em bytes
print(f"codificaçao {nome_completo.encode()}")
#decode() - decodifica para tipo texto comum
print(f"codificaçao {nome_completo.encode().decode()}")

#replace("letra a ser substituida","letra nova a ser colocada no lugar")
print(f" Substitui letra a {nome_completo.replace("e","123")}")
telefone = "(19)97325-0502"
telefone_sem_caracteres_especiais = telefone.replace("(","").replace(")","").replace("-","")
print(f"Telefone sem caracteres especiais: {telefone_sem_caracteres_especiais}")
#join() adiciona um separador a cada caractere no string
print("_".join(nome_completo))
#split() para converter string em listas - o parametro é o caractere alvo para ser usado para dividir
print(f"Nome completo dividido {nome_completo.split(" ")}")
#strip() traz tudo que estiver subjacente a um caractere alvo 
palavra = "xAbacatex"
print(f"Entre os caracteres x{palavra.strip("x")}")
# lstrip() ou rstrip() mesma função acima mas só traz a o texto a partir de determinado caractere
palavra.rstrip("x")
#startswith("parametro") retorna True ou Falso , se a condição do texto começar com o parametro texto informado 
nome_completo.startswith("Re")
# "texto" in "String" (ou) retorna true ou false se a primeira string estiver contida na segunda string. Importante é case sensitive.
#not in ação inversa do in
print("Renat" in nome_completo)


