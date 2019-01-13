import operator
from itertools import product, permutations
import sys 

def mydiv(n, d):
    return n / d if d != 0 else 9999999
 
syms = [operator.add, operator.sub, operator.mul, mydiv] # show operators
op = {sym: ch for sym, ch in zip(syms, '+-*/')}
 
def brute24(nums):
    for x, y, z in product(syms, repeat=3):
        for a, b, c, d in permutations(nums):
            if round(x(y(a,b),z(c,d)),5) == 24:
                return f"({a} {op[y]} {b}) {op[x]} ({c} {op[z]} {d})"
            elif round(x(a,y(b,z(c,d))),5) == 24:
                return f"{a} {op[x]} ({b} {op[y]} ({c} {op[z]} {d}))"
            elif round(x(y(z(c,d),b),a),5) == 24:
                return f"(({c} {op[z]} {d}) {op[y]} {b}) {op[x]} {a}"
            elif round(x(y(b,z(c,d)),a),5) == 24:
                return f"({b} {op[y]} ({c} {op[z]} {d})) {op[x]} {a}"
    return '--Not Found--'

def main(argv):
 
    # make sure there are at least two arguments
    if len(argv) == 4:
        # convert arg 0 and 1 to int and pass them to add function
        hasil = []
        for i in range(len(argv)):
            hasil.append(int(argv[i]))
        print ('\n',brute24(hasil), '\n')
    else:
        print ("\nUsage: python core.spy <number1> <number2> <number3> <number4> \n")
        print ("Example: python sys_argv.py 1 2 3 4\n")
        sys.exit(2) 

if __name__ == '__main__':
    main(sys.argv[1:])
    # num_input = [int(x) for x in sys.argv]
    # num_input = input("add 4 numbers from 1-9, separted by commas:").split(',')

    # print(list_num)
    # print(f"{num_input} -> {brute24(num_input)}")
