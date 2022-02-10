import pyautogui
import time

#configurando pyautogui
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True

#prints
#lava = pyautogui.locateOnScreen('images/lava.png', confidence=0.7)
lava = 'images/lava.png'
lapis = 'images/lapis.png'
diamond = 'images/diamond.png'
coal = 'images/coal.png'
emerald = 'images/emerald.png'
iron = 'images/iron.png'
redstone = 'images/redstone.png'
gold = 'images/gold.png'

#vezes que o botvai rodar
mine_time = 2000
#tempo gasto pars quebrar um bloco
tempo_de_quebrar_com_a_picareta = 0.2

#abrindo o minecraft
pyautogui.click(1160, 1065)
pyautogui.click(971, 452)
pyautogui.press('f11')
time.sleep(3)

#quebrando
def breaking():
    pyautogui.mouseDown(None, None, 'left')

def stop_breaking():
    pyautogui.mouseUp(None, None, 'left')

#reposicionando a tela para quebrar certo
def reposicionando(y):
   pyautogui.move(0, y, 0.1)

#movimentando para frente e parando
def walk():
    pyautogui.keyDown('w')
    reposicionando(-300)
    time.sleep(tempo_de_quebrar_com_a_picareta)
    pyautogui.keyUp('w')
    reposicionando(300)

def stop_walk():
    pyautogui.keyUp('w')

#movendo
def move_screen(x):
    pyautogui.move(x, 0, 1)

#localizando minérios
# def locate_ore(ore):
#     if pyautogui.locateCenterOnScreen(ore, confidence=0.19):
#         print('minerio encontrado')
#         #pyautogui.moveTo(pyautogui.locateCenterOnScreen(ore, confidence=0.29))
#     else:
#         print('sem minério')

#localizando lava
def locate_lava():
    if pyautogui.locateOnScreen(lava, confidence=0.44):
        print('lava encontrada')
        return True
    else:
        print('sem lava')
        return False

#função principal
def main():
    breaking()
    for i in range(0, mine_time):
        #time.sleep(0.5)
        #locate_ore(iron)
        if locate_lava():
            stop_breaking()
            stop_walk()
            pyautogui.keyDown('s')
            time.sleep(2)
            pyautogui.keyUp('s')
            move_screen(58)
            breaking()
        if i == mine_time -1:
            stop_walk()
            stop_breaking()
        
        walk()

        if locate_lava():
            stop_breaking()
            stop_walk()
            pyautogui.keyDown('s')
            time.sleep(2)
            pyautogui.keyUp('s')
            move_screen(58)
            breaking()
        if i == mine_time -1:
            stop_walk()
            stop_breaking()
            
main()
