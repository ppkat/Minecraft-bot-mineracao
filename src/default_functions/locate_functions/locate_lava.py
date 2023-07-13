import pyautogui
from keras.models import load_model
from PIL import Image, ImageOps 
import cv2
import numpy as np

model = load_model('src/training_data/keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
class_names = open("src/training_data/labels.txt", "r").readlines()

#localizando lava
def locate_lava():
    screenshot = pyautogui.screenshot()
    tamanho_da_imagem = (224, 224)
    imagem = ImageOps.fit(screenshot, tamanho_da_imagem, Image.Resampling.LANCZOS)

    imagem_array = np.asarray(imagem)
    imagem_array_normalizada = (imagem_array.astype(np.float32) / 127.5) - 1
    data[0] = imagem_array_normalizada

    predicao = model.predict(data)
    index = np.argmax(predicao)
    class_name = class_names[index]
    pontuacao_de_confianca = predicao[0][index]

    imagem_array_normalizada_uint8 = ((imagem_array_normalizada + 1) * 127.5).astype(np.uint8)

    # Converter a matriz para o formato de imagem
    imagem_normalizada = Image.fromarray(imagem_array_normalizada_uint8)

    # Salvar a imagem em um arquivo
    # caminho_arquivo = "imagem_normalizada.jpg"
    # imagem_normalizada.save(caminho_arquivo)

    # print(predicao)
    # print(class_name[2:])
    
    if 'Lava' in class_name[2:]:
        print('Lava encontrada')
        print(pontuacao_de_confianca)
        return True
    else: return False

# while True:
#     locate_lava()
