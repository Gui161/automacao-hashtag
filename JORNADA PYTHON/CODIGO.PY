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

tabela = pandas.read_csv("JORNADA PYTHON\produtos.csv")
print(tabela)


for linha in tabela.index:
    pyautogui.click(x=648, y=324)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    else:
        pyautogui.write("sem observação")

    pyautogui.press("tab")

    pyautogui.press("enter")      
    pyautogui.press("home")



#Passo 2: Fazer login
#Passo 3: Importar base de dados
#Passo 4: Cadastrar os produtos
#Passo 5: repetir para os produtos
#pyautogui