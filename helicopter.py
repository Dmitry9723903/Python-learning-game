from utils import randcell
import os


TIME_FUEL = 100
class Helicopter:

    def __init__(self, w, h):
        rc=randcell(w, h)
        rx, ry = rc[0], rc[1]
        self.x=rx
        self.y=ry
        self.h=h
        self.w=w
        self.tank = 0
        self.mxtank = 1
        self.score = 0
        self.lives = 30
        self.fuel = 100
    
    def move(self, dx, dy):
        nx, ny = dx + self.x, dy + self.y
        if (nx >= 0 and ny >= 0 and nx < self.h and ny < self.w):
            self.x, self.y = nx, ny
    
    def print_menu(self):
        print("🛢️ ", self.tank, "/", self.mxtank, sep="", end=' | ')
        print('🏆', self.score, end=' | ')
        print('💛', self.lives, end=' | ')
        print('⛽', self.fuel)
    
    def fuel_decreas(self):
        self.fuel -= 1
    
    def game_over(self):
        os.system('cls')
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("----------------------------")
        print("GAME OVER. YOUR SCORE IS:", self.score)
        print("----------------------------")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        exit(0)
    
    def export_data(self):
        return {
            'score': self.score, 
            'lives': self.lives, 
            'fuel': self.fuel, 
            'tank': self.tank, 
            'MXtank': self.mxtank, 
            'x':self.x, 
            'y':self.y,
            }
    
    def import_data(self, data):
        self.x = data['x'] or 0
        self.y = data['y'] or 0
        self.score = data['score'] or 0 
        self.lives = data['lives'] or 30
        self.fuel = data['fuel'] or 100
        self.tank = data['tank'] or 0
        self.mxtank = data['MXtank'] or 1

