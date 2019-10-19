import random
import time
import threading

class blinky:
    def __init__(self):
        self._face = '(o.o)'
    def __str__(self):
        return self._face
    def set_face(self, new):
        self._face = new
        print_blinkies()

    def run(self):
        while True:
            self.set_face('(-.-)')
            time.sleep(random.uniform(.05,.01))
            self.set_face('(o.o)')
            time.sleep(random.expovariate(1/2)) # poisson process equivalent
def print_blinkies():
    for blinky in blinkies:
        print(blinky, end=' ')
        # time.sleep(.001)
    print(end='\r')
blinkies = [blinky() for _ in range(4)]

for blinky in blinkies:
    threading.Thread(target=blinky.run).start()