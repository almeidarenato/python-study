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