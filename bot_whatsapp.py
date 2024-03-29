from distutils.log import error
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import textwrap
import time
from datetime import date
from random import randint
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException


def enter_wpp():
    return (Keys.SHIFT + Keys.ENTER) + Keys.SHIFT


def colar_wpp():
    return (Keys.CONTROL + "v") + Keys.CONTROL


def digitarComoHumano(texto, campo):
    for letra in texto:
        campo.send_keys(letra)
        time.sleep(randint(1, 5)/700)


class WhatsappBot:
    def __init__(self):
        # Parte 1 - A mensagem que você quer enviar
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://web.whatsapp.com')
        self.count_mensagens = 0
        self.count_erros = 0
        self.lorem = textwrap.dedent(
            f"""
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec dictum imperdiet massa ac venenatis. Integer blandit lacus sit amet dolor lacinia viverra. Vestibulum quam odio, feugiat sit amet convallis ut, facilisis fringilla lectus. Duis a leo rutrum, ultrices ipsum vitae, ultricies tortor. Interdum et malesuada fames ac ante ipsum primis in faucibus. Fusce vulputate elit turpis. Nullam dictum eros et odio laoreet, sed ultrices mi lacinia.

          Ut malesuada elit erat, et ultricies urna suscipit et. Nullam at magna velit. Vivamus cursus, felis ut semper mattis, urna ex pulvinar eros, at interdum orci neque vel neque. In hac habitasse platea dictumst. Sed egestas volutpat ipsum tincidunt tempus. Aenean a nunc a mauris accumsan condimentum. Pellentesque placerat mauris ac vestibulum scelerisque. Nam ligula elit, pharetra non lacus vel, vestibulum finibus libero. In nunc libero, iaculis at mollis nec, auctor at turpis. Maecenas in egestas erat. Phasellus tellus augue, scelerisque quis felis tincidunt, consequat sodales lectus. Duis iaculis, lacus ut fringilla lacinia, arcu orci feugiat tortor, eu luctus tellus sapien et lacus. Nam nec nibh augue. Mauris ac convallis ex. Vivamus sit amet quam vitae elit euismod venenatis at vel turpis. Donec auctor fringilla metus, quis aliquam leo feugiat eget.
          """
        )

    def enviarMensagens(self, nomes: list[str], mensagem: str = None):
        flag_continue = input('Deseja continuar? (s/n)')
        if flag_continue == 'n':
            return

        for nome in nomes:
            try:
                time.sleep(2)

                primeiro_nome = nome.capitalize()
                print(primeiro_nome)

                icone_pesquisa = self.driver.find_element(
                    "xpath", "//span[@data-icon='search']")
                icone_pesquisa.click()
                time.sleep(2)

                campo_pesquisa = self.driver.find_element(
                    "xpath", '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]')
                campo_pesquisa.click()
                campo_pesquisa.send_keys(primeiro_nome)
                time.sleep(2)

                campo_grupo = self.driver.find_element(
                    "xpath", f"//span[@title='{nome}'][@class='ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr _11JPr']")
                campo_grupo.click()
                time.sleep(3)

                chat_box = self.driver.find_element(
                    "xpath", '//div[@title="Mensagem"]')
                chat_box.click()

                if mensagem is None:
                    raise ValueError('Mensagem não definida')

                mensagem = mensagem.replace('primeiro_nome', primeiro_nome)
                mensagem = mensagem.replace('\n', enter_wpp())

                # chat_box.send_keys(mensagem + Keys.ENTER)
                
                digitarComoHumano(mensagem + Keys.ENTER, chat_box)
                time.sleep(5)

                self.count_mensagens += 1

            except NoSuchElementException:
                print(f'Nome não encontrado: {nome}')
                with open("names_not_found.txt", "a") as myfile:
                    myfile.write(f"Pessoa não encontrada: {nome}\n")

            except Exception as e:
                print(f'Erro ao enviar a mensagem: {e}')

        return

    def enviarImagem(self, nomes, image_paths):
        time.sleep(18)
        for nome in nomes:
            try:
                icone_pesquisa = self.driver.find_element("xpath",
                                                          "//span[@data-icon='search']")
                icone_pesquisa.click()
                time.sleep(2)
                campo_pesquisa = self.driver.find_element("xpath",
                                                          '//*[@id="side"]/div[1]/div/label/div/div[2]')
                campo_pesquisa.click()
                campo_pesquisa.send_keys(nome)
                time.sleep(2)
                campo_grupo = self.driver.find_element("xpath",
                                                       f"//span[@title='{nome}'][@class='_3ko75 _5h6Y_ _3Whw5']")
                campo_grupo.click()
                time.sleep(3)

                for image_path in image_paths:

                    time.sleep(2)
                    icone_clip = self.driver.find_element("xpath",
                                                          "//div[@title='Anexar']")
                    icone_clip.click()

                    time.sleep(1)
                    icone_imagem = self.driver.find_element("xpath",
                                                            '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                    icone_imagem.send_keys(image_path)

                    time.sleep(4)
                    send_button = self.driver.find_element("xpath",
                                                           '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')
                    send_button.click()

                    time.sleep(2)
                self.count_mensagens += 1
            except Exception:
                print('Erro ao enviar a imagem')
                print(f'Nome não encontrado: {nome}')
                with open("names_not_found.txt", "a") as myfile:
                    myfile.write(f"Pessoa não encontrada: {nome}\n")
                continue

    def enviarMensagemImagem(self, nomes, image_paths, mensagem=None):
        time.sleep(18)
        for nome in nomes:
            try:
                # Parte da mensagem
                primeiro_nome = ((nome.split())[0]).capitalize()
                icone_pesquisa = self.driver.find_element("xpath",
                                                          "//span[@data-icon='search']")
                icone_pesquisa.click()
                time.sleep(2)
                campo_pesquisa = self.driver.find_element("xpath",
                                                          '//*[@id="side"]/div[1]/div/label/div/div[2]')
                campo_pesquisa.click()
                campo_pesquisa.send_keys(nome)
                time.sleep(2)
                campo_grupo = self.driver.find_element("xpath",
                                                       f"//span[@title='{nome}'][@class='_3ko75 _5h6Y_ _3Whw5']")
                campo_grupo.click()
                time.sleep(3)
                chat_box = self.driver.find_element_by_class_name('_3uMse')
                chat_box.click()
                if mensagem == None:
                    mensagem = (
                        textwrap.dedent(
                            f"""
                            Olá {primeiro_nome}, a Cacau Show Plaza Shopping deseja um feliz hoje! 

                            Nossa loja já está aberta, cheia dos deliciosos chocolates que você ama, com atendimento especializado, e montando kits e cestas especiais. Além disso, entregamos para você com todo o conforto e segurança. É tudo muito prático, rápido e feito com carinho.

                            Faça já o seu pedido através da nossa plataforma de delivery ou por WhatsApp!

                            Visite nossa página do Instagram para acessar os links do delivery na bio e confira nosso conteúdo

                            @cacaushow.recife
                            https://www.instagram.com/cacaushow.recife/?hl=pt-br

                            Confira abaixo nosso catálogo
                            """
                        )
                    )
                else:
                    mensagem.replace('primeiro_nome', primeiro_nome)

                mensagem = mensagem.replace('\n', enter_wpp())

                chat_box.send_keys(mensagem)
                time.sleep(5)
                botao_enviar = self.driver.find_element("xpath",
                                                        "//span[@data-icon='send']")
                botao_enviar.click()

                # Parte da imagem
                for image_path in image_paths:

                    time.sleep(2)
                    icone_clip = self.driver.find_element("xpath",
                                                          "//div[@title='Anexar']")
                    icone_clip.click()

                    time.sleep(1)
                    icone_imagem = self.driver.find_element("xpath",
                                                            '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                    icone_imagem.send_keys(image_path)

                    time.sleep(4)
                    send_button = self.driver.find_element("xpath",
                                                           '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')
                    send_button.click()

                    time.sleep(2)
                self.count_mensagens += 1
            except Exception:
                print(f'Nome não encontrado: {nome}')
                with open("names_not_found.txt", "a") as myfile:
                    myfile.write(f"Pessoa não encontrada: {nome}\n")
                continue

    # Inutilizado
    def enviarMensagensLojasImagem(self, nomes, image_path=None):
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
