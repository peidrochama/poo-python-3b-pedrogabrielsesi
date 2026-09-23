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


class Podcast(Conteudo):
    def __init__(self, titulo, genero, episodios):
        super().__init__(titulo, genero)
        self.episodios = episodios

    def exibir_info(self):
        print(f"PODCAST: {self.titulo} | Genero: {self.genero} | Episodios: {self.episodios}")


catalogo = [
    Filme("Invocação do Mal", "Terror", 135),
    Filme("Shrek", "Animacao", 90),
    Serie("Suits", "Advocacia", 9),
    Serie("Round 6", "Suspense", 2),
    Documentario("Nosso Planeta", "Natureza", "Vida selvagem"),
    Documentario("Fire of Love", "Amor e Vulcões", "Amor"),
    Podcast("Flow", "Entrevista", 500)
]

for item in catalogo:
    item.exibir_info()