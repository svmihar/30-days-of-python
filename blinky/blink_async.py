#!/usr/bin/env python
import time
import random
import asyncio


class blinky:
    def __init__(self):
        self._face = '(o.o)'

    def __str__(self):
        return self._face

    def set_face(self, new):
        self._face = new
        print_blinky()
    """ using call_later method, loop it back to each close and open methods """
    # def close_eyes(self, task=None):
    #     self.set_face('(-.-)')
    #     aio_loop_call.call_later(random.uniform(.05, .1), self.open_eyes)

    # def open_eyes(self, task=None):
    #     self.set_face('(o.o)')
    #     aio_loop_call.call_later(random.expovariate(1/2), self.close_eyes)

    async def run(self):
        while True:
            self.set_face('(-.-)')
            await asyncio.sleep(random.uniform(.05, .5))
            self.set_face('(o.o)')
            await asyncio.sleep(random.expovariate(1/2))


def print_blinky():
    for b in blinkies:
        print(b, end='  ')
        time.sleep(.005) # delay works perfectly
    print(end='\r')


blinkies = [blinky() for _ in range(4)]
aio_loop_call = asyncio.get_event_loop()
for b in blinkies:
    # aio_loop_call.call_soon(b.open_eyes)
    asyncio.ensure_future(b.run())
aio_loop_call.run_forever()
