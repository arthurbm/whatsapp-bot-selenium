from bot_whatsapp import WhatsappBot, pd, date
from tkinter import Tk
from tkinter.filedialog import askopenfile
def enviarmsg_loja(nomes, filepath=None):
    bot = WhatsappBot()
    if filepath == None:
        bot.enviarMensagensLojas(nomes)
    else:
        bot.enviarMensagensLojasImagem(nomes, filepath)
    bot.driver.quit()

    with open("text_stored.txt", "a") as myfile:
        myfile.write(f"Número de contatos enviados ({date.today()}) : {bot.count_mensagens}\n")


def fazer_dados():
    df = pd.read_csv('sheets/planilhaVCF2.csv' ,encoding='latin-1', sep=';')

    nomes_completos = (df['NOME E SOBRENOME'].tolist())[158:]

    return nomes_completos

#LEMBRA DE COLOCAR O ÍNDICE DO PRIMEIRO NOME COMO 2
Tk().withdraw() #Keep the root window from appearing
filepath_global = askopenfile()
filepath_name = filepath_global.name
print(filepath_name)
nomes = fazer_dados()
enviarmsg_loja(['Mãe', 'Tio Júnior'], filepath_name)
