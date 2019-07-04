# import os 

e = 0
n=1
while True: 
    n+=1
    e = (1+1/n)**n
    print(e)
    print(f'iteration: {n} \nwith number {e}')
    # os.system('clear')