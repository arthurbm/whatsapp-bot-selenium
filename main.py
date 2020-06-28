from bot_whatsapp import pd, WhatsappBot, date
from tkinter import Tk
from tkinter.filedialog import askopenfile
def enviarmsg(nomes, filepath=None):
    bot = WhatsappBot()
    bot.enviarMensagensLojasImagem(nomes, filepath)
    bot.driver.quit()
    with open("text_stored.txt", "a") as myfile:
        myfile.write(f"Número de contatos enviados ({date.today()}) : {bot.count_mensagens}\n")

filepath_name = ''
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

    opcao = int(input('Digite o número da opção escolhida para quem mandar os opcao:\n1 - Arquivo CSV\n2 - Digitar os nomes'))

    if opcao == 1:
        contatos = fazer_dados()
    elif opcao == 2:
        contatos = input("Digite os nomes exatamente como estão salvos nos contatos separados por uma /\nExemplo: Arthur Brito Medeiros/Pedro Medeiros/Isabela Campelo")
        contatos = contatos.split('/')
    #nomes = fazer_dados()

    opcao_mensagem = int(input('O que você deseja fazer:\n1 - Enviar mensagem e arquivo\n2 - Enviar só mensagem\n3 - Enviar só arquivo'))

    bot2 = WhatsappBot()
    if opcao_mensagem == 1:
        mensagem = input('Escreva a mensagem:\nDica: Escreva no bloco de notas depois cole aqui')
        for nome in contatos:
            try:
                bot2.enviarMensagensLojas(nome, mensagem)
                bot2.enviarImagem()
                if bot2.count_erros >= 2:
                    break
                else:
                    continue
            except Exception:
                print(f'Nome não encontrado: {nome}')
                with open("names_not_found.txt", "a") as myfile:
                    myfile.write(f"Pessoa não encontrada: {nome}\n")
                continue

    if opcao_mensagem == 2:
        mensagem = input('Escreva a mensagem:\nDica: Escreva no bloco de notas depois cole aqui')
        for nome in contatos:
            try:
                bot2.enviarMensagensLojas(nome, mensagem)
            except Exception:
                print(f'Nome não encontrado: {nome}')
                with open("names_not_found.txt", "a") as myfile:
                    myfile.write(f"Pessoa não encontrada: {nome}\n")
                continue

    if opcao_mensagem == 1:
        for nome in contatos:
            bot2.enviarImagem(filepath_name)
            if bot2.count_erros >= 2:
                break
            else:
                continue