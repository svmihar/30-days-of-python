class Dog: 
    def __init__(self, name=" ", age= 0 , furcolor=''): 
        self.name=name
        self.age = age
        self.furcolor = furcolor

    def bark (self, str): 
        print(f'BARK! {str}')
mydog = Dog('Sum',2,'Orange')
mydog.bark('woof')

print(mydog.age)