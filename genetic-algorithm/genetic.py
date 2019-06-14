import random 

from phrase import Phrase, target
from helper import summarize

pop_size = int(input('how many individual in each generation?\n'))
population = []
best_score = 0 
generation = 1 

for i in range(pop_size): 
    population.append(Phrase())

while best_score < len(target): 
    for i in range(pop_size): 
        population[i].get_fitness()

        if population[i].fitness > best_score: 
            best_score = population[i].fitness
            summarize(generation, population[i], best_score)
    
    mating_pool = []
    
    parents = population[:]
    population = []

    ####
    # mating pool is filled with amount of char in fitness variable. 
    ####
    for i in range(pop_size): 
        for j in range(parents[i].fitness): 
            mating_pool.append(parents[i])

    # pick two parents from the pool 
    for i in range(pop_size): 
        x = random.choice(range(len(mating_pool)))
        y = random.choice(range(len(mating_pool)))

    #BREEEEEEED
        child = mating_pool[x].crossover(mating_pool[y])
        child.mutate()

        population.append(child)
    
    generation +=1


