from tokenize import Double
import xlsxwriter
import os

class Planilha():
    def __init__(self,caminhoPlan: str) -> None:
        self.caminho = caminhoPlan
        self.planilha = xlsxwriter.Workbook(caminhoPlan)
        self.sheet = self.planilha.add_worksheet()
    def insereDados(self,moedas:list):
        self.sheet.write("A1", "Moeda")
        self.sheet.write("B1", "Valor")
        row = 1
        col = 0
        for nome,valor in (moedas):
            self.sheet.write(row, col,nome)
            self.sheet.write(row, col+1, valor)     
            row += 1
        
        self.planilha.close()
        os.startfile(self.caminho)