#!/usr/bin/env python

import time
import random
import trio


class blinky:
    def __init__(self):
        self._face = '(o.o)'

    def __str__(self):
        return self._face

    def set_face(self, new):
        self._face = new
        print_blinky()

    async def run(self):
        while True:
            self.set_face('(-.-)')
            await trio.sleep(random.uniform(.05, .5))
            self.set_face('(o.o)')
            await trio.sleep(random.expovariate(1/2))
def print_blinky():
    for b in blinkies:
        print(b, end='    ')
    print(end='\r')

blinkies = [blinky() for _ in range(16)]
async def main():
    async with trio.open_nursery() as n:
        for b in blinkies:
            n.start_soon(b.run)
if __name__ == "__main__":
    trio.run(main)