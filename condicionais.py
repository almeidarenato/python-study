# if , elif e else

# exemplo if/ else - o espaço após o if é importante pois indica que o comando está dentro do if
idade = int(input("Qual a sua idade? Resposta: "))

if idade >= 18:
 print("Você é maior de idade")
elif idade >= 12:
 print("Você é um adolescente")
else:
 print("Você é menor de idade")

 if idade == 19:
  print("Você tem 19 anos")

if idade < 18:
 print("Você é menor de idade")

if idade != 10: 
  print ("Você não tem 10 anos")

# if else em uma linha
  
  mensagem = "Pode tirar carteira de habilitação" if idade >= 18 else "Você não pode tirar a carteira de habilitação"

  print(mensagem)