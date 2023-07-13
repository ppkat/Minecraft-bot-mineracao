import json
import time
import pyautogui

#função para instrução do usuário
def contagem_regressiva():
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)

# Abrir o arquivo config.json e carregar os dados existentes
with open('config.json', 'r') as f:
    config_data = json.load(f)


# coletar a posição do usuário
print('Posicione o mouse no icone do minecraft minimizado na toolbar para coletar a posição')
input("Enter para começar...")
print('A posição será coletada em:')
contagem_regressiva()

coordenadas_icone_do_minecraft = pyautogui.position()
print(f'Posição coletada com sucesso: {coordenadas_icone_do_minecraft}')

print('Agora posicione o mouse na localização para janela inteira (□) da sua aba do minecraft')
input('Enter para começar...')
contagem_regressiva()

coordenadas_maximizar_janela = pyautogui.position()
print(f'Posição coletada com sucesso: {coordenadas_maximizar_janela}')

# Atualizar as coordenadas no objeto de configuração
config_data["coordenadas_icone_do_minecraft"] = [coordenadas_icone_do_minecraft[0], coordenadas_icone_do_minecraft[1]]
config_data["coordenadas_maximizar_janela"] = [coordenadas_maximizar_janela[0],  coordenadas_maximizar_janela[1]]

# Salvar as alterações de volta para o arquivo config.json
with open('config.json', 'w') as f:
    json.dump(config_data, f, indent=4)