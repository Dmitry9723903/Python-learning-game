from utils import randbool
from utils import randcell
from utils import randcell2

CELL_TYPES="🟩🌲🌳🌊🎄🏡🏥✨🔥"

class Map:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells=[[0 for i in range(w)] for j in range(h)]


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
                self.cells[rx2][ry2] = 3
                rx, ry = rx2, ry2
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
    
    def update_fires(self):
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if cell==8:
                    self.cells[ri][ci]=0
        for u in range(10):
            self.add_fire()


    def print_map(self):
        print('⬛' * (self.w + 2))
        for row in self.cells:
            print('⬛', end="")
            for cell in row:
                if (cell>=0 and cell<len(CELL_TYPES)):
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


