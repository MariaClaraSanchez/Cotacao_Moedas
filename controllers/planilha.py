import xlsxwriter
import os
from datetime import date

dia = date.today().strftime("%d-%m-%y")
class Planilha():
    def __init__(self,caminhoPlan: str) -> None:
        self.caminho = caminhoPlan
        self.planilha = xlsxwriter.Workbook(caminhoPlan)
        self.sheetDia = self.planilha.add_worksheet(dia.format())
        
    def insereDados(self,moedas:list):
        self.sheetDia.set_column(0, 1, 25)
        
        formatacao =  self.planilha.add_format({
            'bold': True,
            'border' : 6,
            'align' : 'center',
            'valign' : 'vcenter',
            'size' : 15,
            'fg_color' : 'blue', #Background
            'font_color' : 'white',
        })
        
        self.sheetDia.write("A1", "Moeda",formatacao)
        self.sheetDia.write("B1", "Valor",formatacao)
        
        #set_column(first_col, last_col, width, cell_format, options)
        row = 1
        col = 0
        for nome,valor in (moedas):
            self.sheetDia.write(row, col,nome)
            self.sheetDia.write(row, col+1, valor)     
            row += 1
        
        self.planilha.close()
        os.startfile(self.caminho)