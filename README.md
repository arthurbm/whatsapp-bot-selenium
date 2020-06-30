# WhatsApp bot

Este bot foi projetado para enviar mensagens automáticas, incluindo mídia, para várias pessoas ao mesmo tempo.

Neste código está incluso um arquivo csv_to_vcf.py, que converterá um arquivo CSV em VCF para que os contatos desejados sejam salvos no celular

Ele pode ler um arquivo CSV com todos os nomes de contatos para enviar mensagens e/ou mídia para todos eles ou o usuário pode digita-los manualmente.
(O nome da coluna com os nomes deve ser: "NOMES E SOBRENOMES")

## Tecnologias usadas

- Python
    - Pandas
- Selenium webdriver

## Instalação

Para baixar todos os pacotes, crie um virtual environment usando este comando:

```powershell
python -m venv env_name
```

Ative o virtual enviroment:

```powershell
env_name\Scripts\Activate.ps1
```

Depois disso, use este comando para instalar todos os pacotes necessários:

```powershell
pip install -r requirements.txt
```

## OBS

Se você estiver usando outra versão do chrome diferente de .83 ou outro navegador, você pode fazer o download do driver e substituí-lo pelo disponível para o seu navegador. Lembre-se de mudar o código na parte do bot