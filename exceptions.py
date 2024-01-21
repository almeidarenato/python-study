## Erros que podem ser gerados no programa
print("Exemplo de captura de exceções")

while True:
    try:
        numero = int(input("Informe um número inteiro: "))
        resultado = 10/numero
    except ValueError as error:
        print(f"Erro - valor inválido")
    except ZeroDivisionError as error:
        print(f"Erro - não é possível dividir por 0")
    except Exception as error:
        print(f"Erro:{error}")
        print("Informe um número inteiro válido")
        raise ValueError("Valor informado incompatível")
    else:
        print("Resultado",resultado)
        break
    finally:
        print("-- Programa Finalizado --")