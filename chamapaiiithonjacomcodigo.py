class Pagamento:
    def processar(self):
        print("Processando pagamento")

class Pix(Pagamento):
    def processar(self):
        print("Pagamento via PIX")

class Cartao(Pagamento):
    def processar(self):
        print("Pagamento via cartao")

class Boleto(Pagamento):
    def processar(self):
        print("Pagamento via boleto")

class CarteiraDigital(Pagamento): 
    def processar(self): 
        print("Pagamento via Carteira Digital")

Pagamento = [
Pix(),
Cartao(),
Boleto(),
CarteiraDigital()
]
        
for pagamento in Pagamento:
    pagamento.processar()

    