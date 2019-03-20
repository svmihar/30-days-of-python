weight = int(input('insert weight: '))
jenis = input('L)bs or (K)g: ' )

if jenis == 'k' or jenis == 'K': 
    hasil = weight*0.45
    print(f'you are {hasil} Lbs')
elif jenis == 'l' or jenis=='L': 
    hasil = weight*2.22
    print(f'you are {hasil} kg')
else: 
    print('not a valid input')

print('sucess')


