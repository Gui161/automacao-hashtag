import pyautogui
import time
import pandas

#Passo 1: Entrar no sistema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("chrome")
#time.sleep(3)

pyautogui.press("enter")

pyautogui.click(x=636, y=588)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=628, y=475)
pyautogui.write("luizguilherme_urbaneja@hotmail.com")
pyautogui.press("Tab")
pyautogui.write("12345")
pyautogui.press("Tab")   
pyautogui.press("enter")
time.sleep(3)

tabela = pandas.read_csv("produtos.csv")
print(tabela)

pyautogui.click(x=648, y=324)
#Passo 2: Fazer login
#Passo 3: Importar base de dados
#Passo 4: Cadastrar os produtos
#Passo 5: repetir para os produtos
#pyautogui