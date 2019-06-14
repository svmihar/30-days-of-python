import random 

target = input('INSERT TARGET: ')


class Phrase:
    def __init__(self): 
        self.characters = []
        for i in range(len(target)): 
             self.characters.append(chr(random.choice(range(32,127))))

    def get_content(self): 
        return "".join(self.characters)

    def __str__(self): 
        return "".join(self.characters)

    def get_fitness(self): 
        self.fitness = 0 
        for i in range(len(self.characters)): 
            if self.characters[i] == target[i]: 
                self.fitness+=1

    def crossover(self, partner):
        child = Phrase()
        for i in range(len(self.characters)): 
            if random.random() < .5: 
                child.characters[i] = self.characters[i]
            else: 
                child.characters[i] = partner.characters[i]
        
        return child
    
    def mutate(self): 
        """
        RANDOMLY SWITCH TO ANOTHER CHARACTER.
        mutation_rate = 0.1
        
        *note: seharusnya mutation ratenya berkurang seiring dengan benernya tebakan si child-parent breednya. 
        **note: semakin kecil mutation rate, semakin besar perubahan
        """
        for i in range(len(self.characters)): 
            # .01 is the mutation rate
            if random.random() < .01: 
                self.characters[i] = chr(random.choice(range(32,127)))

