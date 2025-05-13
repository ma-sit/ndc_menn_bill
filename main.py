import pyxel

class main:
    def __init__(self):
        pyxel.init(128, 128, title="naval", fps=30, quit_key=pyxel.KEY_ESCAPE)
        pyxel.load("theme.pyxres")
        self.x=50
        self.y=50
        self.r=0
        self.id=[]
        pyxel.run(self.update, self.draw)
        self.niv=1
        self.can=1
        self.gold=0
        self.nivsuiv=10
        self.xc=None
        self.yc=None
        self.feu=False

    def update(self):
            self.ship()
            self.direction()
            self.tir()

    def draw(self):
        pyxel.cls(5)
        pyxel.blt(self.x, self.y, 0, 35, 2, 10, 12, 5, self.r, 1 )
        pyxel.text(5, 5, f"niveau {self.niv}, {self.can} canon(s) de chaques cotés" , 7)
        pyxel.text(5, 10, f"argent : {self.gold}", 7)
        if self.feu==True:
            pyxel.blt(self.xc, self.yc, 0, 80, 32, 1, 1, )
        
    def ship(self):
        self.id=[]
        if pyxel.btnp(pyxel.KEY_RIGHT,1,2):
            self.x = self.x + 1
            self.r=90
            self.id.append(2)

        if pyxel.btnp(pyxel.KEY_LEFT,1,2):
            self.x = self.x - 1
            self.r=270
            self.id.append(4)

        if pyxel.btnp(pyxel.KEY_UP,1,2):
            self.y = self.y - 1
            self.r=0
            self.id.append(1)

        if pyxel.btnp(pyxel.KEY_DOWN,1,2):
            self.y = self.y + 1
            self.r=180
            self.id.append(3)

    def direction (self):
        if len(self.id)!=1:
            if 1 in self.id:
                if 3 in self.id:
                    self.r=0
                    if 2 in self.id:
                        self.r=90
                    elif 4 in self.id:
                        self.r=270
                elif 2 in self.id:
                    self.r=45
                    if 4 in self.id:
                        self.r=0
                elif 4 in self.id:
                    self.r=315
            elif 2 in self.id:
                if 3 in self.id:
                    self.r=135
                    if 4 in self.id:
                        self.r=180
                elif 4 in self.id:
                    self.r=90
            elif 3 in self.id:
                if 4 in self.id:
                    self.r=225
    
    def tir(self):
        if self.feu==True:
            if self.a != 10:
                self.a += 1
                self.xc = self.xc + self.dir
                self.yc = self.y
            else:
                self.feu = False
                self.a = 0

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT,1,10) and self.feu=False:
            self.feu = True
            self.dir = 5
            self.xc = self.x
            self.yc = self.y

        elif pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT,1,10) and self.feu=False:
            self.feu = True
            self.dir = -5
            self.xc = self.x
            self.yc = self.y


main()