import pyxel

class main:
    def __init__(self):
        pyxel.init(256, 256, title="naval", fps=30, quit_key=pyxel.KEY_ESCAPE)
        pyxel.load("theme.pyxres")
        self.x=128
        self.y=128
        self.r=0
        self.id=[]
        pyxel.run(self.update, self.draw)

    def update(self):
            self.ship()
            self.direction()

    def draw(self):
        pyxel.cls(5)
        pyxel.blt(self.x, self.y, 0, 35, 2, 10, 12, 5, self.r, 1 )
        
    def ship(self):
        self.id=[]
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.x = self.x + 2
            self.r=90
            self.id.append(1)

        if pyxel.btnp(pyxel.KEY_LEFT):
            self.x = self.x - 2
            self.r=270
            self.id.append(2)

        if pyxel.btnp(pyxel.KEY_UP):
            self.y = self.y - 2
            self.r=0
            self.id.append(3)

        if pyxel.btnp(pyxel.KEY_DOWN):
            self.y = self.y + 2
            self.r=180
            self.id.append(4)

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

main()