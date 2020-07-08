from bot_whatsapp import WhatsappBot, date, time, textwrap
import PySimpleGUI as sg
from tkinter import Tk
from tkinter.filedialog import askopenfile
import csv

def fazer_dados_certo():
    print('Escolha o arquivo CSV')
    filepath_global = askopenfile()
    filepath_name = filepath_global.name
    list_names = []
    with open(filepath_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'As colunas sao: {", ".join(row)}')
                line_count += 1
            else:
                list_names.append(f'{row[1]} {row[0]}')
                line_count += 1

        print(f'Processed {line_count} lines.')

    return list_names


#def fazer_dados():
#    print('Escolha o arquivo CSV')
#    filepath_global = askopenfile()
#    filepath_name = filepath_global.name
#    df = pd.read_csv(filepath_name ,encoding='latin-1', sep=';')
#
#    nomes_completos = df['NOME E SOBRENOME'].tolist()
#
#    nomes_completos = sorted(nomes_completos, key = str.lower)
#
#    return nomes_completos

def pedir_mensagem():
    # All the stuff inside your window.
    layout = [  [sg.Text('Escreva a mensagem')],
                [sg.Multiline(size=(40,20), enable_events=True)],
                [sg.Button('Ok')] ]

    # Create the Window
    window = sg.Window('Mensagem', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok': # if user closes window or clicks ok
            break
    window.close()
    return values[0]
    

def num_inputs(msg):
    # All the stuff inside your window.
    layout = [  [sg.Text(msg)],
                [sg.InputText()],
                [sg.Button('Ok')] ]

    # Create the Window
    window = sg.Window('Mensagem', layout)
    # Event Loop to process "events" and get the "values" of the inputs

    event, values = window.read()

    print(values)
    window.close()
    return int(values[0])

def pedir_arquivos(num_files):
    layout = [  [sg.Text('Caminhos dos arquivos')]] 

    list_filepath_send = []
    for x in range(0,num_files):
        layout.append([sg.Input(), sg.FileBrowse()])
    
    layout.append([sg.OK(), sg.Cancel()])

    window = sg.Window('Arquivos', layout)

    event, values = window.read()
    for y in range(0,num_files):
        list_filepath_send.append(values[y])

    print(list_filepath_send)

    window.close()

    return list_filepath_send

#LEMBRA DE COLOCAR O ÍNDICE DO PRIMEIRO NOME COMO 2
def pedir_informacoes():
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

    while ( (opcao != 1 and opcao != 2)):
        opcao = int(input('Digite o número da opção escolhida para o formato que você quer fornecer o nome:\n1 - Arquivo CSV\n2 - Digitar os nomes\n'))

        if opcao == 1:
            contatos = fazer_dados_certo()
            break
        elif opcao == 2:
            contatos = input("Digite os nomes exatamente como estão salvos nos contatos separados por ,\nExemplo: Arthur Brito Medeiros,Pedro Medeiros,Isabela Campelo\n")
            contatos = contatos.split(',')
            break
        else:
            print('Opção inválida, escolha novamente')
        #nomes = fazer_dados()

    while ( (opcao_mensagem != 1 and opcao_mensagem != 2 and opcao_mensagem != 3)):

        opcao_mensagem = int(input('O que você deseja fazer:\n1 - Enviar mensagem e arquivo\n2 - Enviar só mensagem\n3 - Enviar só arquivo\n'))

        if opcao_mensagem == 1:
            mensagem = pedir_mensagem()
            
            num_files = num_inputs('Quantos arquivos você quer enviar')

            list_filepath_send = pedir_arquivos(num_files)

            bot2 = WhatsappBot()
            bot2.enviarMensagemImagem(contatos,list_filepath_send, mensagem)
            bot2.driver.quit()
            with open("number_msg_send.txt", "a") as myfile:
                myfile.write(f"Número de mensagens enviadas: {bot2.count_mensagens}\n")
            break

        elif opcao_mensagem == 2:
            
            mensagem = pedir_mensagem()
            bot2 = WhatsappBot()
            bot2.enviarMensagens(contatos, mensagem)
            bot2.driver.quit()
            with open("number_msg_send.txt", "a") as myfile:
                myfile.write(f"Número de mensagens enviadas: {bot2.count_mensagens}\n")
            break

        elif opcao_mensagem == 3:
            num_files = num_inputs('Quantos arquivos você quer enviar')

            list_filepath_send2 = pedir_arquivos(num_files)
            bot2 = WhatsappBot()
            bot2.enviarImagem(contatos, list_filepath_send2)
            bot2.driver.quit()
            with open("number_msg_send.txt", "a") as myfile:
                myfile.write(f"Número de mensagens enviadas: {bot2.count_mensagens}\n")
            break
        else:
            print('Opção inválida, escolha novamente')

if __name__ == '__main__':
    pedir_informacoes()