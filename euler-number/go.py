# import os 
from itertools import count

# e = 0
# n=1
# while True: 
#     n+=1
#     e = (1+1/n)**n
    # os.system('clear')
c = count()
next(c)
for n in c: 
    print((1+1/n)**n)