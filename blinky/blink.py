import random
import time

class blinky:
    def __init__(self):
        self._face='(o.o)'

    def __str__(self):
        return self._face

    def set_face(self, new):
        self._face = new
        print_blinky(self)

    def run(self):
        while True:
            self.set_face('(-.-)')
            time.sleep(random.uniform(.05, .1))
            self.set_face('(o.o)c')
            time.sleep(random.uniform(.5, 1))

def print_blinky(blinky):
    print('                      ',blinky,end='\r')

if __name__ == "__main__":
    blinky().run()
