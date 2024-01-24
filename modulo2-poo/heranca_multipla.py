# Herança Multipla
class Animal:
    def __init__(self,nome) -> None:
        self.nome = nome
    
    def emitir_som(self):
        pass

class Mamifero:
    def __init__(self,nome) -> None:
        self.nome = nome

    def amamentar(self):
        return f"{self.nome} está amamentando"

class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando"
    
# o super permite chamar o método de uma classe mae. Exemplo :super().emitir_som()
class Morcego(Mamifero,Ave):
    def emitir_som(self):
        return "Morcegos emitem sons ultrassônicos"
    
morcego = Morcego(nome="Morcego")

print(f"Nome do morcego {morcego.nome}")
print(morcego.amamentar())
print(morcego.voar())
print(morcego.emitir_som())