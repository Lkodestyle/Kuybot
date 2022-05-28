import pyautogui as Kuyb
import webbrowser as web

from selenium import webdriver

web.open('https://web.whatsapp.com/send?phone= +549 numero')
Chatlocation=Kuyb.locateAllOnScreen('//*[@id="app"]/div[1]/div[1]/div[4]', confidence=0.9)
()