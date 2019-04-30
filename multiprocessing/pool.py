import time
from multiprocessing import Pool

def sum_square(number): 
    sum = 0
    for i in range(number): 
        sum+=i*i
    return sum

def sum_square_mp(numbers): 
    s = time.time()
    p = Pool()
    result = p.map(sum_square, numbers)
    print(result)

    p.close()
    p.join()

    e = time.time()
    duration = e-s

    print(f'Processing {len(numbers)} took {duration} time using multiprocessing')

def sum_square_no_mp(numbers): 
    s = time.time()

    result = []
    for i in numbers: 
        result.append(sum_square(i))

    e = time.time()
    duration = e-s
    print(f'Processing {len(numbers)} took {duration} time using serial processing')

if __name__ == "__main__":
    numbers = range(10000)
    sum_square_mp(numbers)
    sum_square_no_mp(numbers)
