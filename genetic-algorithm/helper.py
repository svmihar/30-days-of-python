from phrase import target

def summarize(gen, phr, fit): 

    print(f'Generation #{gen:3}: ', end='')
    print(phr)
    print(f'score {fit:2}/{len(target)}')    