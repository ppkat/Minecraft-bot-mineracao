import pyautogui
import time

tempo_de_quebrar_com_a_picareta = 0.8
voltando = False

#quebrando
def breaking():
    pyautogui.mouseDown(None, None, 'left')

#movendo
def move_screen(x):
    pyautogui.move(x, 0, 1)

#reposicionando a tela para quebrar certo
def reposicionando(y):
   pyautogui.move(0, y, 0.1)

def stop_breaking():
    pyautogui.mouseUp(None, None, 'left')

def stop_walk():
    pyautogui.keyUp('w')

def andar_pra_frente():
    if(voltando): return
    else: pyautogui.keyDown('w')

#movimentando para frente e parando
def walk():
    andar_pra_frente()
    reposicionando(-200)
    time.sleep(tempo_de_quebrar_com_a_picareta)
    pyautogui.keyUp('w')
    reposicionando(200)
    time.sleep(tempo_de_quebrar_com_a_picareta)

def meia_volta():
    voltando = True
    stop_breaking()
    stop_walk()
    pyautogui.keyDown('s')
    time.sleep(2)
    pyautogui.keyUp('s')
    move_screen(58)
    breaking()
    voltando = False