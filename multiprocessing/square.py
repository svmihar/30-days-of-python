import os, time
from multiprocessing import Process, current_process

def square(numbers): 
    for number in numbers: 
        # time.sleep(0.3)
        result = number**2
        print(f'the numbers {number} squares to {result}')

    # process_id = os.getpid()
    # print(f'Print process id: {process_id}')
    # process_name = current_process().name
    # print(f'current process name: {process_name}')


if __name__ == "__main__":
    processes = []
    numbers = range(100)
    for i in range(2): 
        process = Process(target=square, args=(numbers,))
        processes.append(process)

        process.start()

    for process in processes: 
        process.join()
    
    print('Multiprocessing completed')
