import time, logging
from multiprocessing import Process, Lock, Value
from multiprocessing import log_to_stderr, get_logger


def add_500_no_lock(total): 
    for i in range(100): 
        time.sleep(0.01)
        total.value += 5


def sub_500_no_lock(total): 
    for i in range(100): 
        time.sleep(0.01)
        total.value -= 5

def add_500_lock(total, lock): 
    for i in range(100): 
        time.sleep(0.01)
        lock.acquire()
        total.value += 5
        lock.release()

def sub_500_lock(total, lock): 
    for i in range(100): 
        time.sleep(0.01)
        lock.acquire()
        total.value -= 5
        lock.release()


if __name__ == "__main__":
    total = Value('i', 500)
    lock = Lock()

    log_to_stderr()
    logger = get_logger()
    logger.setLevel(logging.INFO) # WHAT IS THIS?

    add_process = Process(target=add_500_lock, args=(total, lock))
    sub_process = Process(target=sub_500_lock, args=(total, lock))

    add_process.start()
    sub_process.start()

    add_process.join()
    sub_process.join()

    print(total.value)
