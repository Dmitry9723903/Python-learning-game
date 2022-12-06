# 🎄, 🟩, 🌲, 🌳, 🏡, 🌊, ⬛, 🏥, ✨, 🔥, 🚁, 🛢️, 🏆
from map import Map
import time
import os
from helicopter import Helicopter as Helico
from pynput import keyboard

TICK_SLEEP=0.005
SPRUCE_TREE_UPDATE=250
CHRISTMAS_TREE_UPDATE=300
FIRE_UPDATE=600
VILLAS_UPDATE=1000
MAP_W, MAP_H=20, 20


tmp = Map(MAP_W, MAP_H)

helico=Helico(MAP_W, MAP_H)

MOVES = {'w':(-1, 0), 'd':(0, 1), 's':(1, 0), 'a':(0,-1)}

def process_key(key):
    global helico
    c=key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)

listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()

tick = 1
while True:
    os.system("cls")
    print("TICK", tick)
    tmp.process_helicipter(helico)
    helico.print_menu()
    tmp.print_map(helico)
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



