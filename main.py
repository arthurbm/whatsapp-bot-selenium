from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import time

def enter_wpp():
    return (Keys.SHIFT + Keys.ENTER) + Keys.SHIFT

class WhatsappBot:
    def __init__(self):
        # Parte 1 - A mensagem que você quer enviar
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.driver = webdriver.Chrome()
        self.driver.get('https://web.whatsapp.com')

    def enviarMensagens(self,nomes,mensagem):
        time.sleep(20)
        for nome in nomes:
            icone_pesquisa = self.driver.find_element_by_xpath("//span[@data-icon='search']")
            icone_pesquisa.click()
            time.sleep(2)
            campo_pesquisa = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
            campo_pesquisa.click()
            campo_pesquisa.send_keys(nome)
            time.sleep(2)
            campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='{nome}'][@class='_1wjpf _3NFp9 _3FXB1']")
            campo_grupo.click()
            time.sleep(2)
            chat_box = self.driver.find_element_by_class_name('_1Plpp')
            chat_box.click()
            chat_box.send_keys(mensagem)
            time.sleep(6)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            botao_enviar.click()
            time.sleep(5)
    
    def enviarMensagensLojas(self,nomes):
        time.sleep(20)
        for nome in nomes:
            primeiro_nome = ((nome.split())[0]).capitalize()
            icone_pesquisa = self.driver.find_element_by_xpath("//span[@data-icon='search']")
            icone_pesquisa.click()
            time.sleep(2)
            campo_pesquisa = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
            campo_pesquisa.click()
            campo_pesquisa.send_keys(nome)
            time.sleep(2)
            campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='{nome}'][@class='_1wjpf _3NFp9 _3FXB1']")
            campo_grupo.click()
            time.sleep(2)
            chat_box = self.driver.find_element_by_class_name('_1Plpp')
            chat_box.click()
            mensagem = (
                f'Hey {primeiro_nome}, tá se programando pra assistir as lives do final de semana, ou vai assistir maratonar uma série na Netflix? Vim aqui pra te lembrar que o Mr Hoppy Rui barbosa combina com todos esses estilos e muito mais!'+ enter_wpp()  +
                'Dá uma olhada na nossa playlist do Spotify pra escutar antes das suas lives favoritas:' + enter_wpp()  +
                'link-spotify'+ enter_wpp()  + enter_wpp() +
                'Faça já o seu pedido por Whatsapp (Esse mesmo) , telefone, Ifood, ou Rappi!'+ enter_wpp()  + enter_wpp() +

                'Telefone:'+ enter_wpp()  +
                '30973109'+ enter_wpp()  + enter_wpp() +

                'Ifood:'+ enter_wpp()  +
                'https://www.ifood.com.br/delivery/recife-pe/mr-hoppy-rui-barbosa-gracas/882b8026-f499-462b-994f-77cdd546a8d4'+ enter_wpp() + enter_wpp()  + 
                
                'Rappi:'+ enter_wpp()  + 
                'https://rappi.app.link/UkNOKoWPf6 (Para celulares)'+ enter_wpp()  +
                'ou'+ enter_wpp()  +
                'https://www.rappi.com.br/restaurantes/mr-hoppy-rui-barbosa (Para computadores)'
                
            )
            chat_box.send_keys(mensagem)
            time.sleep(6)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            botao_enviar.click()
            time.sleep(5)

    #O usuario seleciona manualmente a mensagem e o bot manda de uma vez
    def encaminharMensagens(self,sobrenome):
        time.sleep(20)
        botao_encaminhar = self.driver.find_element_by_xpath("//span[@data-icon='forward']")
        botao_encaminhar.click()
        chat_box = self.driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[1]/div/label/div/div[2]')
        chat_box.click()
        chat_box.send_keys(sobrenome)
        time.sleep(5)
        #scroll_box = self.driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[2]')
        #self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scroll_box)
        links = self.driver.find_elements_by_class_name('_1mFmt')
        for clickable in links:
            if clickable != '':
                clickable.click()
                time.sleep(1)

df = pd.read_csv('planilhaVCF2.csv' ,encoding='latin-1', sep=';')

nomes_completos = df['NOME E SOBRENOME']

bot = WhatsappBot()
bot.enviarMensagensLojas(nomes_completos)
bot.driver.quit()
