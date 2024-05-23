#passo a passo do projeto

# 1. abrir o sistema da empresa

# https://dlp.hashtagtreinamentos.com/python/intensivao/login
#abrir o navegador
#buscar o site do sistema da empresa
#importar a biblioteca
import pandas as pd
import pyautogui
import time 
pyautogui.PAUSE = 1.0
#clicar com mouse --> pyautogui.click
#escrever um texto --> pyautogui.write
#clicar no botão --> pyautogui.press
#apertar um conjunto de teclas --> pyautogui.hotkey

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# pode ser que ele demore alguns segundos para carregar o site
time.sleep(4)






# 2. fazer login

pyautogui.click(x=693, y=377)

pyautogui.write('mfaucz@gmail.com')

pyautogui.press('tab')

pyautogui.write('flamengo100')

pyautogui.press('enter')

time.sleep(3)

# 3. abrir/importar a base de dados de produtos para cadastrar


tabela_produtos = pd.read_csv('produtos.csv')

print(tabela_produtos) 




# 4. cadastrar o produto

for linha in tabela_produtos.index:


    codigo_produto = str((tabela_produtos.loc[linha, 'codigo']))

    #clicar no campo do codigo do produto

    pyautogui.click(x=591, y=274)

    #preencher o codigo

    pyautogui.write(codigo_produto)


    #passar pro proximo campo

    pyautogui.press('tab')


    #marca
    pyautogui.write (str(tabela_produtos.loc[linha, 'marca']))
    pyautogui.press('tab')
    #tipo
    pyautogui.write (str(tabela_produtos.loc[linha, 'tipo']))
    pyautogui.press('tab')
    #categoria
    pyautogui.write (str(tabela_produtos.loc[linha, 'categoria']))
    pyautogui.press('tab')
    #preço
    pyautogui.write (str(tabela_produtos.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    #custo
    pyautogui.write (str(tabela_produtos.loc[linha, 'custo']))
    pyautogui.press('tab')
    #observação
    obs = str(tabela_produtos.loc[linha, 'obs'])

    if obs != 'nan':

        pyautogui.write(obs)
    pyautogui.press('tab')
    #apertar o botao
    pyautogui.press('enter')

    pyautogui.scroll(5000)





# 5. Repetir isso tudo até acabar a lista de produtos