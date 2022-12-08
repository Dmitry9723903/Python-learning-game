# 🎄, 🟩, 🌲, 🌳, 🏡, 🌊, ⬛, ⭐, ✨, 🔥, 🚁, 🛢️, 🏆, 💛, ⛽,  ⚪(clouds), 🔵(lightnings), 
from map import Map
from clouds import Cloud
import time
import os
import json
from helicopter import Helicopter as Helico
from pynput import keyboard

TICK_SLEEP=0.005
SPRUCE_TREE_UPDATE=250
CHRISTMAS_TREE_UPDATE=300
FIRE_UPDATE=600
CLOUDS_UPDATE=700
VILLAS_UPDATE=1000
MAP_W, MAP_H=20, 20
TIME_FUEL = 100

tmp = Map(MAP_W, MAP_H)
clouds=Cloud(MAP_W, MAP_H)
helico=Helico(MAP_W, MAP_H)
tick = 1

MOVES = {'w':(-1, 0), 'd':(0, 1), 's':(1, 0), 'a':(0,-1)}

def process_key(key):
    global helico, tick, clouds, tmp
    c=key.char.lower()

    # обработка движения вертика
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)
    # сохранение игры
    elif c=='f':
        data={'Helicopter':helico.export_data(), 
                     'Map':tmp.export_data(), 
                  'Clouds':clouds.export_data(),
                    'tick':tick
        }
        with open('level.json','w') as lvl:
            json.dump(data, lvl)
    # загрузка игры
    elif c=='g':
        with open('level.json', 'r') as lvl:
            data = json.load(lvl)
            tick = data['tick'] or 1
            helico.import_data(data['Helicopter'])
            tmp.import_data(data['Map'])
            clouds.import_data(data['Clouds'])
            

listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()


while True:
    os.system("cls")
    tmp.process_helicipter(helico, clouds)
    helico.print_menu()
    tmp.print_map(helico, clouds)
    print("TICK", tick)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TICK_SLEEP == 0):
        tmp.generate_deciduous_tree()
    if (tick % SPRUCE_TREE_UPDATE == 0):
        tmp.generate_spruce_tree()
    if (tick % CHRISTMAS_TREE_UPDATE == 0):
        tmp.generate_Сhristmas_tree()
    if (tick % VILLAS_UPDATE == 0):
        tmp.add_villas()
    if (tick % FIRE_UPDATE == 0):
        tmp.update_fires()
    if (tick % TIME_FUEL == 0):
        helico.fuel_decreas()
        if (helico.fuel<=0):
            helico.game_over()
    if (tick % CLOUDS_UPDATE == 0):
        clouds.update_clouds()


    
    

