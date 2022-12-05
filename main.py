# 🎄, 🟩, 🌲, 🌳, 🏡, 🌊, ⬛, 🏥, ✨, 🔥
from map import Map
import time
import os


TICK_SLEEP=0.005
SPRUCE_TREE_UPDATE=50
CHRISTMAS_TREE_UPDATE=200
FIRE_UPDATE=100
VILLAS_UPDATE=300
MAP_W, MAP_H=20, 20

tmp = Map(MAP_W, MAP_H)
tmp.generate_coniferous_forests(1, 10)
tmp.generate_forests(2, 10)
tmp.generate_rivers(30)
tmp.generate_rivers(3)
tmp.generate_rivers(3)
tmp.generate_villas(1, 80)
tmp.print_map()

tick = 1
while True:
    os.system("cls")
    print("TICK", tick)
    tmp.print_map()
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



