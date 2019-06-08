from csp import Constraint, CSP 
from typing import Dict, List, Optional 

class SendMoreMoney(Constraint[str, int]): 
    def __init__(self, letters) -> None: 
        super().__init__(letters)
        self.letters = letters
    def satisfied(self, assignment)-> bool: 
        # check kalo ada duplikat, kalo gak ada berarti itu solusinya. 
        if len(set(assignment.values())) < len(assignment): 
            return False

        # jika semua variabel sudah assigned check jika itu bener nambahnya
        if len(assignment) == len(self.letters): 
            s = assignment['S']
            e = assignment['E']
            n = assignment['N']
            d = assignment['D']
            m = assignment['M']
            o = assignment['O']
            r = assignment['R']
            y = assignment['Y']
            send: int = n*1000 + e * 100 + n*10 + d
            more: int = m * 1000 + o*100 + r*10 + e
            money: int  = m * 10000 + o*1000 + n*100 + e*10 + y
            return send + more == money

        return True # no conflict here 

if __name__ == "__main__":
    letter = 'S E N D M O R Y'
    letters = letter.split()
    possible_digits = {}
    for letter in letter: 
        possible_digits[letter] = [x for x in range(10)]
    possible_digits['M'] = [1] # supaya gak mulai dari 0 
    csp = CSP(letters, possible_digits)
    csp.add_constraint(SendMoreMoney(letters))
    solution = csp.backtracking_search()

    if solution is None: 
        print('No solution is found')
    else: 
        print(solution)