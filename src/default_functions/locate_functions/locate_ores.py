#localizando minérios
def locate_ore(ore):
    if pyautogui.locateCenterOnScreen(ore, confidence=0.19):
        print('minerio encontrado')
        #pyautogui.moveTo(pyautogui.locateCenterOnScreen(ore, confidence=0.29))
    else:
        print('sem minério')