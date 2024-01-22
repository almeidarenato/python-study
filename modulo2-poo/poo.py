# Linguagem de programação orientada a objetos - POO
# POO - Paradigma de programação que se baseia na organização de programas em torno de objetos
# Objetos são instâncias de classes
# Permite que se crie programas de formula modular , reutilizável e mais fácil de se entender

# Os pilares do POO são - Encapsulamento , Herança , Polimorfismo e abstração
# Desvantagem do POO - para aplicações simples adiciona uma carga de complexidade desnecessária


# Classe
# Modelo que se define a estrutura dos objetos
# __init__ é o método construtor no python
# self é uma referencia a sua própria classe
# --> None é opcional. Define que o método não tem retorno.
# métodos são ações ou comportamentos da classe. Sempre é necessário referenciar o self



class Pessoa:
    def __init__(self,nome,idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return(f"Olá meu nome é {self.nome} e eu tenho {self.idade} anos")


# Objetos são instancias concretas da classe e podem representar objetos do mundo real
pessoa = Pessoa("Renato","30")
print(pessoa.saudacao())
print(pessoa.nome,pessoa.idade)