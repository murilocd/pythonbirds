class Pessoa:
    olhos = 2 # atributo de classe, comum a todos objetos
              ## __dict__não enxerga. Enxerga somente atributos de instância

    def __init__(self, *filhos, nome, idade=36):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == "__main__":
    murilo = Pessoa(nome="Murilo Pai")
    cesar = Pessoa(murilo, nome="Cesar Filho") ## murilo é filho de cesar

    print(Pessoa.cumprimentar(murilo))
    print(cesar.nome)

    for filho in cesar.filhos:
        print(filho.nome)

    cesar.sobrenome = "Drumond" ## criado atributo dinâmico
    del cesar.filhos ##removido atributo dinâmico
    # atributos dinâmicos = atributos criados em tempo de execução, específico para um objeto ou situação
    print(cesar.__dict__) # método que exibe os atributos de cada objeto (instancia)
    print(murilo.__dict__)