from controllers.acessar_google import SiteGoogle
from controllers.config import Config
from controllers.planilha import Planilha

def start():
    config = Config.get_config()
    google = SiteGoogle(config['site']['driver'])
    moedas = google.acessar_google()

    print(moedas)
    # print(type(moedas))
    
    planilha = Planilha(config['planilha']['caminho'])
    planilha.insereDados(moedas)    

if __name__ == '__main__':
    start()