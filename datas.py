
class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print("{}/{}/{}".format(self.dia, self.mes, self.ano))


d = Data(0o5, 10, 1990)
d.formatada()

