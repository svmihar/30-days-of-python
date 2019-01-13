a,b,c=0,0,0
for i in range(100):
    i=i+1
    if (i%5==0 and i%3==0):
        print("fizzbuzz")
        c+=1
    elif i%5==0:
        print("buzz")
        b+=1
    elif(i%3==0):
        print("buzz")
        a+=1
    print(i)
print("counter", "\nfizz={}".format(a), "\nbuzz= {}".format(b),"\nfizzbuzz = {}".format(c))
print("total= {}".format(a+b+c))