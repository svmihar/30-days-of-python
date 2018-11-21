from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        print('Running my_logger on {}'.format(orig_func.__name__))
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        print('saved to logger')
        return orig_func(*args, **kwargs)
    
    return wrapper

def my_timer(orig_func):
    import time
    @wraps(orig_func) #digunakan supaya yang di return bukan wrapper, tapi orig_func, biar gak pusing penamaan buat yang di return 
    def wrapper(*args, **kwargs): 
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('my_timer: {} ran in: {} sec'.format(orig_func.__name__, t2))
        return result
    return wrapper

import time

#urutan dari '@' itu penting, kalo kebalik nanti kebalik2 juga return function nya 
@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info = my_logger(my_timer(display_info))
display_info('tian.RAR', 22)