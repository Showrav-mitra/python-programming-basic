w= input("weight=  ")
perimeter = input('lbs or kg = ')
if perimeter == 'l':
    convert = int(w) * 0.4
    print(f'weight in lbs = {convert}')

elif perimeter == 'k':
    convert =int(w) * 1000
    print(f'weight is kg = {convert}')

else :
    print('weight is = ', w)