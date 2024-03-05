# Step by Step
# 1 - Enter in the system
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

    # you do only once: pip install pyautogui

import pyautogui
import time
import pandas

pyautogui.PAUSE = 1

    # pyautogui.click() -> click somewhere in he screen
    # pyautogui.write() -> write a text
    # pyautogui.press() -> press one key from keyboard
    # pyautogui.hotkey("key1", "key2") -> press a combination of keys from keyboard

# open the browser (opera)
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

# enter the site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# give a bigger pause (3 seconds)
time.sleep(3)

# 2 - do the login

# user
pyautogui.click(x=2109, y=405)
pyautogui.write("pythonpowerupjourney@somemail.com")

# password
pyautogui.press("tab")
pyautogui.write("somepasswordhere")

# click on "logar" button
pyautogui.click(x=2290, y=563)
time.sleep(3)

# you can also do that by using keyboard with the commands:
# pyautogui.press("tab")
# pyautogui.press("enter")

# 3 - import the data base
table = pandas.read_csv("produtos.csv")

# 4 - register a product
# for each row in the products table
for rows in table.index:

    # click on first field
    pyautogui.click(x=2039, y=293)

    # "codigo do produto" field
    pyautogui.write(str(table.loc[rows, "codigo"]))
    pyautogui.press("tab")

    # "marca" field
    pyautogui.write(str(table.loc[rows, "marca"]))
    pyautogui.press("tab")

    # "tipo" field
    pyautogui.write(str(table.loc[rows, "tipo"]))
    pyautogui.press("tab")

    # "categoria" field
    pyautogui.write(str(table.loc[rows, "categoria"]))
    pyautogui.press("tab")

    # "preco" field
    pyautogui.write(str(table.loc[rows, "preco_unitario"]))
    pyautogui.press("tab")

    # "custo" field
    pyautogui.write(str(table.loc[rows, "custo"]))
    pyautogui.press("tab")

    # "obs" field
    obs = table.loc[rows, "obs"]
    if not pandas.isna(obs):     
        pyautogui.write(obs)
    pyautogui.press("tab")

    # "enviar" button
    pyautogui.press("enter")

    # go back to the top scrolling (use a very high number to scroll)
    pyautogui.scroll(8000)

# 5 - repeat the process of registering until the end of the data base