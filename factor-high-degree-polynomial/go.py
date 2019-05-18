from math import sqrt

def gcd(a,b):
    while b:
        a,b = b, a % b
    return a

def simplify(num, den):
    if den == 0:
        return "div by 0 - result not found"

    div = gcd(num,den)
    (reduced_num,  reduced_den) = (num / div, den/div)
    if div == 1:
        return (num, den)
    else:
        if(reduced_den > den):
            if(reduced_den * reduced_num < 0):
                return (-reduced_num, -reduced_den) # biar positif
            else:
                return (reduced_num, reduced_den)
        else:
            return(reduced_num, reduced_den)
def quad(a,b,c):
    if(b*b-4*a*c >= 0):
        x1 = (-b + sqrt(b*b-4*a*c))/(2*a)
        x2 = (-b - sqrt(b*b-4*a*c))/(2*a)

        m1 = -x1 * a
        m2 = -x2 * a
        (num1,den1) = simplify(a,m1)
        (num2,den2) = simplify(a,m2)

        if((num1 > a) or (num2 > a)):
            print('nothing')
        else:
            if(den1 > 0):
                sign1 = "+"
            else:
                sign1 = ""
            if(den2 > 0):
                sign2 = "+"
            else:
                sign2 = ""
            print(f'({int(num1)}x{sign1}{int(den1)})({int(num1)}x{sign2}{int(den2)})')
    else:
        print("working on the imaginaries")

quad(1,4,4)
