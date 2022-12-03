from utils import randbool
from utils import randcell
from utils import randcell2

CELL_TYPES="🟩🌲🌳🌊🎄🏡🏥✨"

class Map:
    def print_map():
        pass

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

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells=[[0 for i in range(w)] for j in range(h)]
        pass

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
        if x < 0 or y < 0 or x >=self.h or y >= self.w:
            return False
        else:
            return True


tmp = Map(30, 30)
tmp.generate_coniferous_forests(1, 10)
tmp.generate_forests(2, 10)
tmp.generate_rivers(30)
tmp.generate_rivers(10)
tmp.generate_rivers(3)
tmp.generate_rivers(3)
tmp.print_map()
    