
################################## Projeto Feito no Jupyter notebook - dia 06/12/2022 - Lucas de Oliveira Martins ##################################

#    **Automatizar um processo com a linguagem Python:**

# - Instalar e utilizar bibliotecas
# - Buscar dados de ações automaticamente
# - Gerar algumas estatísticas com esses dados
# - Gerar um gráfico simples de linha    
# - Automatizar o controle do teclado e mouse com o **pyautogui**    
# - Utilizar strings de múltiplas linhas
#   Enviar e-mails de forma automática
    
    
# -   **Projeto da aula:**
# - Você trabalha em uma empresa de investimentos e todos os dias precisa enviar um e-mail com o valor da cotação de algumas ações. O e-mail precisa conter as informações dos últimos seis meses:
# - Cotação mínima da ação
# - Cotação máxima da ação
# - Cotação do dia
    

# Let's Start
## Passo 1

!pip install yfinance

import yfinance

ticker = input("Digite a sigla da ação desejada: ") #Exemplo: PETR4.SA
dados = yfinance.Ticker(ticker).history("6mo")
fechamento = dados.Close
fechamento.plot()

##Passo 2

maxima = fechamento.max()
minima = fechamento.min()
atual = fechamento[-1]

##Passo 3

!pip install pyautogui
!pip install pyperclip

import pyautogui
import pyperclip

#Abrir o gmail digitar o texto e enviar

pyautogui.PAUSE = 2

pyautogui.hotkey("ctrl", "t")
pyperclip.copy("www.gmail.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")
pyautogui.click(x=132, y=194)

pyperclip.copy("fulano@gmail.com")
pyautogui.click(x=908, y=308)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

pyperclip.copy("Análises diárias")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

mensagem = f"""
Prezado Fulano,

Seguem as análises dos últimos seis meses da ação {ticker}:

Cotação máxima: R$ {round(maxima, 2)}
Cotação mínima: R$ {round(minima, 2)}
Cotação atual: R$ {round(atual, 2)}

Qualquer dúvida estou à disposição!
"""
    
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

pyautogui.hotkey("ctrl", "enter")
pyautogui.hotkey("ctrl", "w")
print("Email enviado com sucesso!")

#Puxar posição do mouse
#import time
#time.sleep(3)
#print("Posição do Cursor")
#pyautogui.position()




