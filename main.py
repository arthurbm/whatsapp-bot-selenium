from bot_whatsapp import pd, WhatsappBot, date, time, textwrap
from tkinter import Tk
from tkinter.filedialog import askopenfile

def fazer_dados():
    print('Escolha o arquivo CSV')
    filepath_global = askopenfile()
    filepath_name = filepath_global.name
    df = pd.read_csv(filepath_name ,encoding='latin-1', sep=';')

    nomes_completos = df['NOME E SOBRENOME'].tolist()

    nomes_completos = sorted(nomes_completos, key = str.lower)

    return nomes_completos

#LEMBRA DE COLOCAR O ÍNDICE DO PRIMEIRO NOME COMO 2
def pedir_informacoes():
    flag = False
    flag2 =False
    opcao = 0
    opcao_mensagem = 0
    mensagem_inicio = textwrap.dedent(
            '''
            Olá! Esse é um bot que manda mensagem automaticamentes pelo Whatsapp, como se fosse um ser humano, mas de forma automática e ediciente.

            Para se referir ao primeiro nome de uma pessoa em uma mensagem escreva o termo primeiro_nome que ele será substituído pelo primeiro nome do contato.

            Exemplo: (Para um contato chamado Arthur Brito)
            input: Olá, primeiro_nome, tudo bem?
            Output: Olá Arthur, tudo bem?
            '''
        )
    print(mensagem_inicio)

    while ( (opcao != 1 and opcao != 2) or (flag == False) ):
        opcao = int(input('Digite o número da opção escolhida para o formato que você quer fornecer o nome:\n1 - Arquivo CSV\n2 - Digitar os nomes\n'))

        if opcao == 1:
            contatos = fazer_dados()
            flag = True
        elif opcao == 2:
            contatos = input("Digite os nomes exatamente como estão salvos nos contatos separados por uma /\nExemplo: Arthur Brito Medeiros/Pedro Medeiros/Isabela Campelo\n")
            contatos = contatos.split('/')
            flag = True
        else:
            print('Opção inválida, escolha novamente')
        #nomes = fazer_dados()

    while ( (opcao != 1 and opcao != 2 and opcao != 3) or (flag2 == False) ):

        opcao_mensagem = int(input('O que você deseja fazer:\n1 - Enviar mensagem e arquivo\n2 - Enviar só mensagem\n3 - Enviar só arquivo\n'))

        if opcao_mensagem == 1:
            mensagem = input('Escreva a mensagem:\nDica: Escreva no bloco de notas depois cole aqui\n')
            print('Escolha o arquivo')
            filepath = askopenfile()
            filepath_send = filepath.name
            bot2 = WhatsappBot()
            bot2.enviarMensagemImagem(contatos, mensagem, filepath_send)
            flag2 =True
            bot2.driver.quit()
            with open("number_msg_send.txt", "a") as myfile:
                myfile.write(f"Número de mensagens enviadas: {bot2.count_mensagens}\n")

        elif opcao_mensagem == 2:
            mensagem = input('Escreva a mensagem:\nDica: Escreva no bloco de notas depois cole aqui\n')
            bot2 = WhatsappBot()
            bot2.enviarMensagens(contatos, mensagem)
            flag2 = True
            bot2.driver.quit()
            with open("number_msg_send.txt", "a") as myfile:
                myfile.write(f"Número de mensagens enviadas: {bot2.count_mensagens}\n")

        elif opcao_mensagem == 3:
            print('Escolha o arquivo')
            filepath = askopenfile()
            filepath_send_2 = filepath.name
            bot2 = WhatsappBot()
            bot2.enviarImagem(contatos, filepath_send_2)
            flag2 = True
            bot2.driver.quit()
            with open("number_msg_send.txt", "a") as myfile:
                myfile.write(f"Número de mensagens enviadas: {bot2.count_mensagens}\n")
        else:
            print('Opção inválida, escolha novamente')

if __name__ == '__main__':
    pedir_informacoes()