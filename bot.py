import tkinter as tk
import threading
import pyautogui as pag
import time

FULL_SCREEN_REGION = 0, 0, 960, 1050
CENTER_SCREEN = 480, 480
MANA_TO_SPELL = 100
running = False  # Variável para controlar a execução das funções

#TODO: mover show_cordinates e print_region para outro código
# Função para mostrar as coordenadas do mouse
def show_coordinates():
    global running
    running = True
    while running:
        x, y = pag.position()
        print(f'Mouse Coordinates: X={x}, Y={y}')
        time.sleep(1)

# Função para tirar uma captura de tela
def print_region():
    screenshot = pag.screenshot(region=FULL_SCREEN_REGION)
    screenshot.save('screenshot.png')



# Função para comer
def auto_eater():
    global running
    running = True
    while running:
        fish = pag.locateOnScreen('fish.png')
        if fish is not None:
            center_fish = pag.center(fish)
            pag.moveTo(center_fish)
            pag.click(button='right')
        time.sleep(1)
        #TODO: definir timer para autoeater

# Função para arrastar
def move_blank():
    global running
    running = True
    while running:
        blank = pag.locateOnScreen('blank.png')
        if blank is not None:
            center_blank = pag.center(blank)
            hand = pag.locateOnScreen('hand.png')
            if hand is not None:
                center_hand = pag.center(hand)
                pag.moveTo(center_blank)    
                pag.dragTo(center_hand)
        time.sleep(1)

# Função para pescar
def auto_fish():
    global running
    running = True
    while running:
        fishing_rod = pag.locateOnScreen('fishing_rod.png')
        water = pag.locateOnScreen('water.png', confidence=0.8)
        if fishing_rod is not None and water is not None:
            center_rod = pag.center(fishing_rod)
            center_water = pag.center(water)
            pag.moveTo(center_rod)
            time.sleep(1)
            pag.click(button='right')
            pag.moveTo(center_water)
            time.sleep(1)
            pag.click(button='left')
        time.sleep(1)
        #TODO: definir tempo do autoeat

# Função para lançar um feitiço
def cast_spell():
    pag.moveTo(CENTER_SCREEN)
    pag.press('9')
    #TODO: só deve rodar com x mana




#TODO: mover gui para outro código
# Função para iniciar a execução de uma função em uma thread separada
def start_function(func):
    global running
    running = True
    thread = threading.Thread(target=func)
    thread.start()

# Função para parar a execução
def stop_function():
    global running
    running = False

# Interface gráfica
root = tk.Tk()
root.title("Auto Functions")

# Botões para cada função
btn_show_coords = tk.Button(root, text="Show Coordinates", command=lambda: start_function(show_coordinates))
btn_show_coords.pack(pady=5)

btn_print_region = tk.Button(root, text="Print Region", command=print_region)
btn_print_region.pack(pady=5)

btn_auto_eater = tk.Button(root, text="Auto Eater", command=lambda: start_function(auto_eater))
btn_auto_eater.pack(pady=5)

btn_move_blank = tk.Button(root, text="Move Blank", command=lambda: start_function(move_blank))
btn_move_blank.pack(pady=5)

btn_auto_fish = tk.Button(root, text="Auto Fish", command=lambda: start_function(auto_fish))
btn_auto_fish.pack(pady=5)

btn_cast_spell = tk.Button(root, text="Cast Spell", command=cast_spell)
btn_cast_spell.pack(pady=5)

# Botão para parar as funções
btn_stop = tk.Button(root, text="Stop", command=stop_function)
btn_stop.pack(pady=5)

root.mainloop()
