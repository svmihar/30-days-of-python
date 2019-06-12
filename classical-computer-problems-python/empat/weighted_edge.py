from __future__ import annotations
from dataclasses import dataclass
from empat.edge import Edge
"""
Sebenernya ini mirip dengan yang edge cuman ini ada weighted nya aja tiap path nya. 

"""

@dataclass
class WeightedEdge(Edge): 
    weight: float 

    def reversed(self): 
        return WeightedEdge(self.v, self.u, self.weight)
    
    #order edges by weight default python function 
    # implementation of < operator. 
    def __lt__(self, other: WeightedEdge) -> bool: 
        return self.weight < other.weight
        
    # biar cantik kalo di print()
    def __str__(self): 
        return f'{self.u} {self.weight} > {self.v}'

    
    

