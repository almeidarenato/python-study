# Linguagem de programação orientada a objetos - POO
# POO - Paradigma de programação que se baseia na organização de programas em torno de objetos
# Objetos são instâncias de classes
# Permite que se crie programas de formula modular , reutilizável e mais fácil de se entender

# Classe
# Modelo que se define a estrutura dos objetos
# __init__ é o método construtor no python
# self é uma referencia a sua própria classe
# --> None é opcional. Define que o método não tem retorno.


class Pessoa:
    def __init__(self,nome,idade) -> None:
        self.nome = nome
        self.idade = idade