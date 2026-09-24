class Conteudo:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero

    def exibir_info(self):
        print(f"Titulo: {self.titulo} | Genero: {self.genero}")


class Filme(Conteudo):
    def __init__(self, titulo, genero, duracao):
        super().__init__(titulo, genero)
        self.duracao = duracao

    def exibir_info(self):
        print(f"FILME: {self.titulo} | Genero: {self.genero} | Duracao: {self.duracao} minutos")


class Serie(Conteudo):
    def __init__(self, titulo, genero, temporadas):
        super().__init__(titulo, genero)
        self.temporadas = temporadas

    def exibir_info(self):
        print(f"SERIE: {self.titulo} | Genero: {self.genero} | Temporadas: {self.temporadas}")


class Documentario(Conteudo):
    def __init__(self, titulo, genero, tema):
        super().__init__(titulo, genero)
        self.tema = tema

    def exibir_info(self):
        print(f"DOCUMENTARIO: {self.titulo} | Genero: {self.genero} | Tema: {self.tema}")


# Testando
filme1 = Filme("Invocação do Mal", "terror", 135)
serie1 = Serie("Suits", "Advocacia", 9)
documentario1 = Documentario("Nosso Planeta", "Natureza", "Vida selvagem")

filme1.exibir_info()
serie1.exibir_info()
documentario1.exibir_info()
#exemplo edição
