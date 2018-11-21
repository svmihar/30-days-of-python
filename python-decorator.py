
#cloures
def outer_function(msg):
    def inner_function(): 
        print(msg)
    return inner_function

hi_func = outer_function('hi')
bye_func = outer_function('bye')

hi_func()
bye_func()
#end

#basic decorator function
#decorators: function as an argument in a function an return a function
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs): #wrapper digunakan sebagai medium "komunikasi" antar scope dari fungsinnya
        print("wrapper executed this shit {}".format(original_function.__name__))
        return original_function(*args, **kwargs) #catatan: accept all numbers of arguments
    return wrapper_function

@decorator_function
def display(): 
    print('display function called')

display()


def display_info(name, age):
    print('display info ran with arguments ({}, {}) '.format(name, age))

#decorated_display = decorator_function(display)
# decorated_display()

display_info("svmihar", 17)

#end

#class decorator
class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before ({})', format(self.original_function.__name__))
        return self.original_function(*args, **kwargs) 

@decorator_class #jarang dipake walaupun bisa 
def display_info_class(name, age):
    print('display info ran with arguments ({}, {}) '.format(name, age))
display_info_class('yan', 21)
