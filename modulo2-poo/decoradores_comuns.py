# Decoradores comuns

#@classmethod
#@staticmethod

class MinhaClasse:
    valor = 10 # atributo da classe

    def __init__(self,nome) -> None:
        self.nome = nome
    
    #requer uma instância para ser chamado
    def metodo_instancia(self):
        return f"Método de instância chamado para {self.nome}"
    @classmethod
    def metodo_classe(cls):
        return f"Método de classe chamado para valor= {cls.valor}"
    
    @staticmethod #não recebe atributos da instância nem da classe. Pode ser usado para calcular um valor
    def metodo_estatico():
        return "método estático chamado"


obj = MinhaClasse(nome="Teste")
print(obj.metodo_instancia()) # para chamar o método eu preciso de uma instancia para ser chamado
print(MinhaClasse.valor) # Como é um atributo da classe não preciso de uma instância
print(MinhaClasse.metodo_classe()) # consigo chamar um método apenas com a classe com o decorator @classmethod
print(MinhaClasse.metodo_estatico()) #consigo chamar o método apenas com a classe com o decorator @staticmethod porém sem acesso aos atributos

# Método classmethod pode ser usado para criar instâncias da classe

class Carro:
    def __init__(self,marca,modelo,ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls,configuracao):
        marca,modelo,ano = configuracao.split(",")
        return cls(marca,modelo,int(ano))
    
carro = Carro.criar_carro("Toyota,Corolla,2022")
print(f"{carro.marca}\n{carro.modelo}\n{carro.ano}")

# O @classmethod é muito usado em bibliotecas
# Se há muitos métodos estáticos é um sinal de má prática, portanto não se deve criar muitos métodos estáticos

class Matematica:
    @staticmethod
    def somar(a,b):
        return a+b
    
print(Matematica.somar(a=19,b=19))