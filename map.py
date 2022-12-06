from utils import randbool
from utils import randcell
from utils import randcell2

CELL_TYPES="🟩🌲🌳🌊🎄🏡🏥✨🔥"
TREE_BOUNS = 100
UPGRADE_COST = 500

class Map:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells=[[0 for i in range(w)] for j in range(h)]
        self.generate_coniferous_forests(1, 10)
        self.generate_forests(2, 10)
        self.generate_rivers(30)
        self.generate_rivers(3)
        self.generate_rivers(3)
        self.generate_villas(1, 80)
        self.upgrade_shope()


    def generate_coniferous_forests(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci]=1

    def generate_forests(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci]=2
    
    def generate_villas(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci]=5


    def generate_rivers(self, l):
        rc = randcell(self.w, self.h)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry]=3
        while l>0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if (self.chack_bounds(rx2, ry2)):
                rx, ry = rx2, ry2
                self.cells[rx2][ry2] = 3
                l -= 1

    def generate_Сhristmas_tree(self):
        c=randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.cells[cx][cy]==0):
            self.cells[cx][cy]=4

    def generate_spruce_tree(self):
        c=randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.cells[cx][cy]==0):
            self.cells[cx][cy]=1

    def generate_deciduous_tree(self):
        c=randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.cells[cx][cy]==0):
            self.cells[cx][cy]=2

    def add_villas(self):
        c=randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.cells[cx][cy]==0):
            self.cells[cx][cy]=5

    def add_fire(self):
        c=randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.cells[cx][cy] == 1 or self.cells[cx][cy] == 2 or self.cells[cx][cy] == 4 or self.cells[cx][cy] == 5):
            self.cells[cx][cy]=8
    
    def upgrade_shope(self):
        c=randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.cells[cx][cy]==0):
            self.cells[cx][cy]=7

    def update_fires(self):
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if cell==8:
                    self.cells[ri][ci]=0
        for u in range(8):
            self.add_fire()


    def print_map(self, helico):
        print('⬛' * (self.w + 2))
        for ri in range(self.h):
            print('⬛', end="")
            for ci in range(self.w):
                cell=self.cells[ri][ci]
                if (helico.x==ri and helico.y==ci):
                    print('🚁', end="")
                elif (cell>=0 and cell<len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end="")
#                if cell==0:
#                    print('🟩', end="")
#                elif cell==1:
#                    print('🌲', end="")
#                elif cell==2:
#                    print('🌳', end="")
#                elif cell==3:
#                    print('🌊', end="")
#                elif cell==4:
#                    print('🎄', end="")
#                elif cell==5:
#                    print('🏡', end="")
#                elif cell==6:
#                    print('🏥', end="")
#                elif cell==7:
#                    print('✨', end="")       
            print('⬛', end="")
            print()  
        print('⬛' * (self.w + 2))

    def chack_bounds(self, x, y):
        if (x < 0 or y < 0 or x >=self.h or y >= self.w):
            return False
        else:
            return True

    def process_helicipter(self, helico):
        c=self.cells[helico.x][helico.y]
        if (c==3):
            helico.tank = helico.mxtank
        elif (c==8 and helico.tank>0):
            helico.tank -= 1
            helico.score += TREE_BOUNS
            self.cells[helico.x][helico.y]=1
        elif (c==7 and helico.score >= UPGRADE_COST):
            helico.score -= UPGRADE_COST
            helico.mxtank += 1



