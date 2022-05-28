import pyautogui as Kuyb
import time
import webbrowser as web
import pandas as pd
from time import sleep


#1
web.open('https://web.whatsapp.com/send?phone= +54 9 numero')
time.sleep(10)
ScreenWidht,ScreenHeight=Kuyb.size()
CurrentMouseX,CurrentMouseY=Kuyb.position
Kuyb.moveTo(850,1000)
Kuyb.click()
time.sleep(2)
Kuyb.write('Hola')
Kuyb.press('enter')
time.sleep(2)
Kuyb.hotkey('ctrl' , 'w')



