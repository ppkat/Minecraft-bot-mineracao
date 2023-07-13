import pyautogui
import threading
import json
from default_functions.locate_functions.locate_lava import locate_lava
from default_functions.action_functions import *

#configurando pyautogui
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True

#coletando do arquivo de configurações as posições dos icones
with open('config.json', 'r') as f:
    config_data = json.load(f)

x_maximizar = config_data["coordenadas_icone_do_minecraft"][0]
y_maximizar = config_data["coordenadas_icone_do_minecraft"][1]
x_extender = config_data["coordenadas_maximizar_janela"][0]
y_extender = config_data["coordenadas_maximizar_janela"][1]

#vezes que o bot vai rodar
mine_time = 2000

#abrindo o minecraft
pyautogui.click(x_maximizar, y_maximizar) #as cordenadas do icone do minecraft minimizado
time.sleep(0.2)

#botando em janela cheia
pyautogui.click(x_extender, y_extender) #cordenados do icone de modo janela extendida
time.sleep(4)

# despausando
pyautogui.press('esc')
time.sleep(1)

#função principal
def main():
    # Iniciar a thread para procurar lava
    # lava_thread = threading.Thread(target=search_for_lava)
    # lava_thread.start()

    breaking()
    for i in range(0, mine_time):
        walk()

        if locate_lava():
            meia_volta()

        if i == mine_time -1:
            stop_walk()
            stop_breaking()

# def search_for_lava():
#     while True:
#         if locate_lava():
#             meia_volta()
main()
