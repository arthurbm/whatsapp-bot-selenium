from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import textwrap
import time
from datetime import date
from random import randint
import traceback

def enter_wpp():
    return (Keys.SHIFT + Keys.ENTER) + Keys.SHIFT
def colar_wpp():
    return (Keys.CONTROL + "v") + Keys.CONTROL
def digitarComoHumano(texto, campo):
        for letra in texto:
            campo.send_keys(letra)
            time.sleep(randint(1,5)/1200)
class WhatsappBot:
    def __init__(self):
        # Parte 1 - A mensagem que você quer enviar
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.get('https://web.whatsapp.com')
        self.count_mensagens = 0
        self.count_erros = 0
    
    def enviarMensagens(self,nomes, mensagem=None):
        time.sleep(18)
        for nome in nomes:
            try:
                time.sleep(2)

                primeiro_nome = ((nome.split())[0]).capitalize()
                icone_pesquisa = self.driver.find_element_by_xpath("//span[@data-icon='search']")
                icone_pesquisa.click()
                time.sleep(2)
                campo_pesquisa = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
                campo_pesquisa.click()
                campo_pesquisa.send_keys(nome)
                time.sleep(2)
                campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='{nome}'][@class='_3ko75 _5h6Y_ _3Whw5']")
                campo_grupo.click()
                time.sleep(3)
                chat_box = self.driver.find_element_by_class_name('_3uMse')
                chat_box.click()
                if mensagem == None:
                    mensagem = (
                        textwrap.dedent(
                            f"""
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec dictum imperdiet massa ac venenatis. Integer blandit lacus sit amet dolor lacinia viverra. Vestibulum quam odio, feugiat sit amet convallis ut, facilisis fringilla lectus. Duis a leo rutrum, ultrices ipsum vitae, ultricies tortor. Interdum et malesuada fames ac ante ipsum primis in faucibus. Fusce vulputate elit turpis. Nullam dictum eros et odio laoreet, sed ultrices mi lacinia.

                            Ut malesuada elit erat, et ultricies urna suscipit et. Nullam at magna velit. Vivamus cursus, felis ut semper mattis, urna ex pulvinar eros, at interdum orci neque vel neque. In hac habitasse platea dictumst. Sed egestas volutpat ipsum tincidunt tempus. Aenean a nunc a mauris accumsan condimentum. Pellentesque placerat mauris ac vestibulum scelerisque. Nam ligula elit, pharetra non lacus vel, vestibulum finibus libero. In nunc libero, iaculis at mollis nec, auctor at turpis. Maecenas in egestas erat. Phasellus tellus augue, scelerisque quis felis tincidunt, consequat sodales lectus. Duis iaculis, lacus ut fringilla lacinia, arcu orci feugiat tortor, eu luctus tellus sapien et lacus. Nam nec nibh augue. Mauris ac convallis ex. Vivamus sit amet quam vitae elit euismod venenatis at vel turpis. Donec auctor fringilla metus, quis aliquam leo feugiat eget.
                            """
                        )
                    )
                mensagem = mensagem.replace('\n', enter_wpp())
                
                digitarComoHumano(mensagem, chat_box)
                time.sleep(5)
                botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                botao_enviar.click()
                self.count_mensagens += 1
            except Exception:
                traceback.print_exc()
                print('Erro ao enviar a mensagem')
                print(f'Nome não encontrado: {nome}')
                with open("names_not_found.txt", "a") as myfile:
                    myfile.write(f"Pessoa não encontrada: {nome}\n")
                continue

    def enviarImagem(self,nomes, image_path):
        time.sleep(18)
        for nome in nomes:
            try:

                icone_pesquisa = self.driver.find_element_by_xpath("//span[@data-icon='search']")
                icone_pesquisa.click()
                time.sleep(2)
                campo_pesquisa = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
                campo_pesquisa.click()
                campo_pesquisa.send_keys(nome)
                time.sleep(2)
                campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='{nome}'][@class='_3ko75 _5h6Y_ _3Whw5']")
                campo_grupo.click()
                time.sleep(3)

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
                self.count_mensagens += 1
            except Exception:
                traceback.print_exc()
                print('Erro ao enviar a imagem')
                print(f'Nome não encontrado: {nome}')
                with open("names_not_found.txt", "a") as myfile:
                    myfile.write(f"Pessoa não encontrada: {nome}\n")
                continue
    
    def enviarMensagemImagem(self, nomes, mensagem, image_path):
        time.sleep(18)
        for nome in nomes:
            try:
                #Parte da mensagem
                primeiro_nome = ((nome.split())[0]).capitalize()
                icone_pesquisa = self.driver.find_element_by_xpath("//span[@data-icon='search']")
                icone_pesquisa.click()
                time.sleep(2)
                campo_pesquisa = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
                campo_pesquisa.click()
                campo_pesquisa.send_keys(nome)
                time.sleep(2)
                campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='{nome}'][@class='_3ko75 _5h6Y_ _3Whw5']")
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
                else:
                    mensagem = mensagem.replace('primeiro_nome', primeiro_nome)
                mensagem = mensagem.replace('\n', enter_wpp()) 
                
                digitarComoHumano(mensagem, chat_box)
                time.sleep(5)
                botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                botao_enviar.click()
                #Parte da imagem
                time.sleep(2)
                icone_clip = self.driver.find_element_by_xpath("//div[@title='Anexar']")
                icone_clip.click()
                
                time.sleep(1)
                icone_imagem = self.driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                icone_imagem.send_keys(image_path)

                time.sleep(4)
                send_button = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')
                send_button.click()

                time.sleep(2)
                self.count_mensagens += 1
            except Exception:
                traceback.print_exc()
                print(f'Nome não encontrado: {nome}')
                with open("names_not_found.txt", "a") as myfile:
                    myfile.write(f"Pessoa não encontrada: {nome}\n")
                continue

        
    #Inutilizado
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
                
                if self.count_erros >= 5:
                    break
                else:
                    continue
                
            