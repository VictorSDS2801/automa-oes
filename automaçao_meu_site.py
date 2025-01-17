import pyautogui
import time

#intervalo entre as açoes
pyautogui.PAUSE = 0.5
#entrar no navegador
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
#indo pro site
pyautogui.write("https://me-conte-sobre-voce.netlify.app")
pyautogui.press("enter")
time.sleep(1)
#respondendo pergunta 1
pyautogui.moveTo(x=434, y=306, duration = 0.5)
pyautogui.click()
pyautogui.write("Victor Diogo Santos de Araujo")
time.sleep(1)
#repondendo pergunta 2
pyautogui.moveTo(x=1527, y=409, duration = 0.5)
pyautogui.click()
pyautogui.moveTo(x=159, y=458, duration = 0.5)
pyautogui.click()
pyautogui.moveTo(x=172, y=522, duration = 0.5)
pyautogui.scroll(7000)
pyautogui.moveTo(x=110, y=602, duration = 0.5)
pyautogui.click()
pyautogui.moveTo(x=124, y=523, duration = 0.5)
pyautogui.click()
pyautogui.moveTo(x=232, y=639, duration = 0.5)
pyautogui.click()
#respondendo pergunta 3
pyautogui.moveTo(x=196, y=508, duration = 0.5)
pyautogui.click()
pyautogui.moveTo(x=173, y=441, duration = 0.5)
pyautogui.scroll(-500)
pyautogui.click()
#respondendo a pergunta 4
pyautogui.moveTo(x=298, y=608, duration = 0.5)
pyautogui.click()
pyautogui.write("victordiogo2801@gmail.com")
pyautogui.moveTo(x=370, y=672, duration = 0.5)
pyautogui.click()
pyautogui.write("Victor2801@")
pyautogui.scroll(-700)
#repondendo a pergunta 5
pyautogui.moveTo(x=82, y=175, duration = 0.5)
pyautogui.click()
pyautogui.moveTo(x=82, y=250, duration = 0.5)
pyautogui.click()
#respondendo a pergunta 6
pyautogui.moveTo(x=182, y=391, duration = 0.5)
pyautogui.click()
#respondendo a pergunta 7
pyautogui.moveTo(x=149, y=770, duration = 0.5)
pyautogui.click()
pyautogui.moveTo(x=431, y=163, duration = 0.5)
pyautogui.click()
pyautogui.moveTo(x=634, y=447, duration = 0.5)
pyautogui.click()
#respondendo pergunta 8
pyautogui.scroll(-50000)
pyautogui.moveTo(x=183, y=545, duration = 0.5)
pyautogui.click()
pyautogui.write("Victor Diogo Santos de Araujo")
pyautogui.moveTo(x=292, y=624, duration = 0.5)
pyautogui.click()
pyautogui.write("Obrigado por ter visto meu site e enviar feedback!")
pyautogui.moveTo(x=157, y=690, duration = 0.5)
pyautogui.click()
pyautogui.moveTo(x=991, y=168, duration = 0.5)
pyautogui.click()
#indo pra o outro site
pyautogui.scroll(-500000)
pyautogui.moveTo(x=915, y=813, duration = 0.5)
pyautogui.click()          
