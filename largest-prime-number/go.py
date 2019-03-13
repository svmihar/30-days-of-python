
import math 
  

def maxPrimeFactors (n): 

    maxPrime = -1
    while n % 2 == 0: 
        maxPrime = 2
        n >>= 1     # equivalent to n /= 2 
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i == 0: 
            maxPrime = i 
            n = n / i 
    if n > 2: 
        maxPrime = n 
    return int(maxPrime) 
  
def is_prime(n): 
    if n==1: 
        return False 
    max_divisor = math.floor(math.sqrt(n))
    for d in range(2,1+max_divisor): 
        if n % d == 0: 
            return False

    return True

prime_numbers = []
import time
t0 = time.time()
for i in range(1,1000000): 
    if is_prime(i): 
        prime_numbers.append(i)

print('time required: ', time.time() - t0)
print(prime_numbers)
print(len(prime_numbers))
