class CompressedGene: 
    def __init__(self, gene: str): -> None
        self._compress(gene) # _compress berarti private method, damn you PEP 8 
    for nucleotide in gene.upper(): 
        self.bit_string <<=2 #shift left 2 bits (bitwise operator)
        if nucleotide=='A':  
            self.bit_string |= 0b00
        elif nucleotide =='C': 
            self.bit_string |= 0b01
        elif nucleotide=='T': 
            self.bit_string |= 0b11
        elif nucleotide=='G': 
            self.bit_string |= 0b10
        else: 
            raise ValueError("Invalid nucleotide input: {}".format(nucleotide))