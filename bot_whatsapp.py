from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import textwrap
import time
from datetime import date
import traceback

def enter_wpp():
    return (Keys.SHIFT + Keys.ENTER) + Keys.SHIFT
def colar_wpp():
    return (Keys.CONTROL + "v") + Keys.CONTROL
class WhatsappBot:
    def __init__(self):
        # Parte 1 - A mensagem que você quer enviar
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.get('https://web.whatsapp.com')
        self.count_mensagens = 0
        self.count_erros = 0
    
    def enviarMensagensLojas(self,nome, mensagem=None):
        time.sleep(20)

        primeiro_nome = ((nome.split())[0]).capitalize()
        icone_pesquisa = self.driver.find_element_by_xpath("//span[@data-icon='search']")
        icone_pesquisa.click()
        time.sleep(2)
        campo_pesquisa = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        campo_pesquisa.click()
        campo_pesquisa.send_keys(nome)
        time.sleep(2)
        campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='{nome}'][@class='_3ko75 _5h6Y_ _3Whw5']")
        print(campo_grupo)
        campo_grupo.click()
        time.sleep(3)
        chat_box = self.driver.find_element_by_class_name('_3uMse')
        chat_box.click()
        if mensagem == None:
            mensagem = (
                textwrap.dedent(
                    f"""
                    Olá {primeiro_nome}, 
                    esse é uma mensagem de teste
                    """
                )
            )
        mensagem = mensagem.replace('\n', enter_wpp())
        
        chat_box.send_keys(mensagem)
        time.sleep(5)
        botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        botao_enviar.click()
        self.count_mensagens += 1

    def enviarImagem(self, image_path):
        try:
            time.sleep(2)
            icone_clip = self.driver.find_element_by_xpath("//div[@title='Anexar']")
            icone_clip.click()
            
            time.sleep(1)
            icone_imagem = self.driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
            icone_imagem.send_keys(image_path)

            time.sleep(4)
            send_button = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')
            send_button.click()

            time.sleep(3)
        except Exception:
            traceback.print_exc()
            print('Erro ao enviar a imagem')
            self.count_erros+=1
        

    def enviarMensagensLojasImagem(self,nomes, image_path = None):
        time.sleep(15)
        count_erros = 0
        for nome in nomes:
            try:
                self.enviarMensagensLojas(nome)
            except Exception:
                print(f'Nome não encontrado: {nome}')
                with open("names_not_found.txt", "a") as myfile:
                    myfile.write(f"Pessoa não encontrada: {nome}\n")
                continue

            if image_path != None:
                self.enviarImagem(image_path)
                
                if self.count_erros >= 2:
                    break
                else:
                    continue
                
            