from utils import randbool
from utils import randcell
from utils import randcell2

#'π©', cell==0 ; 'π²', cell==1; 'π³', cell==2; 'π', cell==3; 'π',cell==4; 'π‘', cell==5; 'β­'(Hospital) cell==6,'β¨' (upgrade shope), cell==7;
#'π₯' cell==8, 'β½' (fuel station) cell==9

CELL_TYPES="π©π²π³πππ‘β­β¨π₯β½"
TREE_BOUNS = 100
UPGRADE_COST = 500
LIVE_COST = 1000

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
        self.upgrade_hospital()
        self.add_fuel_station()
        self.add_fuel_station()
        self.add_fuel_station()


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

    def generate_Π‘hristmas_tree(self):
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
    
    def add_fuel_station(self):
        c=randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.cells[cx][cy]==0):
            self.cells[cx][cy]=9

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
    
    def upgrade_hospital(self):
        c=randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.cells[cx][cy]==0):
            self.cells[cx][cy]=6

    def update_fires(self):
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if cell==8:
                    self.cells[ri][ci]=0
        for u in range(8):
            self.add_fire()


    def print_map(self, helico, clouds):
        print('β¬' * (self.w + 2))
        for ri in range(self.h):
            print('β¬', end="")
            for ci in range(self.w):
                cell=self.cells[ri][ci]
                if (clouds.cells[ri][ci]==1):
                    print('βͺ', end="")
                elif (clouds.cells[ri][ci]==2):
                    print('π΅', end="")  
                elif (helico.x==ri and helico.y==ci):
                    print('π', end="")
                elif (cell>=0 and cell<len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end="")
            print('β¬', end="")
            print()  
        print('β¬' * (self.w + 2))

    def chack_bounds(self, x, y):
        if (x < 0 or y < 0 or x >=self.h or y >= self.w):
            return False
        else:
            return True

    def process_helicipter(self, helico, clouds):
        c=self.cells[helico.x][helico.y]
        d=clouds.cells[helico.x][helico.y]
        if (c==3):
            helico.tank = helico.mxtank
        elif (c==8 and helico.tank>0):
            helico.tank -= 1
            helico.score += TREE_BOUNS
            self.cells[helico.x][helico.y]=1
        elif (c==7 and helico.score >= UPGRADE_COST):
            helico.score -= UPGRADE_COST
            helico.mxtank += 1
        elif (c==6 and helico.score >= LIVE_COST):
            helico.score -= LIVE_COST
            helico.lives += 10
        elif (c==9 and helico.score >=UPGRADE_COST):
            helico.score -= UPGRADE_COST
            helico.fuel += 100
        elif (d==2):
            helico.lives -= 1
            if (helico.lives<=0):
                helico.game_over()

    def export_data(self):
        return {
            'cells':self.cells
        }
    
    def import_data(self, data):
        self.cells = data['cells'] or [[0 for i in range(self.w)] for j in range(self.h)]

