from bot_whatsapp2 import WhatsappBot, pd, date
from tkinter import Tk
from tkinter.filedialog import askopenfile
def enviarmsg(nomes, filepath=None):
    bot = WhatsappBot()
    bot.enviarMensagensLojasImagem(nomes, filepath)
    bot.driver.quit()
    with open("text_stored.txt", "a") as myfile:
        myfile.write(f"Número de contatos enviados ({date.today()}) : {bot.count_mensagens}\n")


def fazer_dados():
    df = pd.read_csv('sheets/planilhaVCF2.csv' ,encoding='latin-1', sep=';')

    nomes_completos = (df['NOME E SOBRENOME'].tolist())[158:]

    return nomes_completos

#LEMBRA DE COLOCAR O ÍNDICE DO PRIMEIRO NOME COMO 2

Tk().withdraw()#Keep the root window from appearing
filepath_global = askopenfile()
filepath_name = filepath_global.name
print(filepath_name)
print(type(filepath_name))

#nomes = fazer_dados()
enviarmsg(['Mãe', 'Tio Júnior', 'teste' ,'Pai Tim'], filepath_name)
