# Pilares da Programação Orientada a Objeto
# Abstração , Encapsulamento, Herança e Polimorfismo

# Herança e Polimorfismo

#pass pode ser usado quando há necessidade de criar uma função vazia.

class Animal:
    def __init__(self,nome) -> None:
        self.nome = nome
    
    def andar(self):
        print(f"O animal {self.nome} andou")
        return
    
    def emitir_som(self):
        pass 

# classe herdando a classe mãe
# polimorfismo permite reimplementar métodos da classe mãe , ou seja permite ter outro comportamento, apesar do mesmo nome
    
class Cachorro(Animal):
    def emitir_som(self):
        return "Au, au"

class Gato(Animal):
    def emitir_som(self):
        return "Miau!"
    
dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")
print(dog.emitir_som())
print(cat.emitir_som())
animais = [dog,cat]

for animal in animais:
    print(f"O {animal.nome} emite o som: {animal.emitir_som()}")

# Exemplo de encapsulamento
# eu garanto que estou manipulando o valor desta variável de uma maneira correta
    
class ContaBancaria:
    def __init__(self,saldo) -> None:
        self.__saldo = saldo # Atributo privado definido como "__" antes do nome. Ninguem terá acesso fora da classe
    
    def depositar(self,valor):
        if valor >0:
            self.__saldo += valor
    
    def sacar(self,valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
    
    def consultar_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(saldo=1000)
print(f"saldo da conta bancária {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(f"saldo da conta bancária {conta.consultar_saldo()}")
conta.depositar(valor=-500) ## não será permitido
print(f"saldo da conta bancária {conta.consultar_saldo()}")
conta.sacar(500)
print(f"saldo da conta bancária {conta.consultar_saldo()}")

# Abstração
# Uma classe abstrata não permite criar instancias a partir dela diretamente. 
# Ela é apenas um molde que obriga quem herda a implementar seus métodos.
# Exemplo de abstração

# a classe abstrata não implementa nada. É apenas um molde.
from abc import ABC, abstractmethod

class Veiculo(ABC):
    
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
       pass

class Carro(Veiculo):
    def __init__(self) -> None:
        pass

    def ligar(self):
        return "Carro ligado usando a chave"
    
    def desligar(self):
        return "Carro desligado usando a chave"

carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())

# Exemplo real de abstração
# Acesso a banco de dados e retornos
# Podemos usar uma classe abstrata com os métodos usados para trazer dados do banco
# E ter diversas instancias com diferentes bacnos de dados. 