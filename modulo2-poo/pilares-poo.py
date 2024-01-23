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
    
