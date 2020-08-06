a = 1
b = 'SSS'
c = True
l = [1, 2, 3, 4, 'ssss']
d = b + 'Hello'
t = (1, 2, 3, 4)
dt = {
    'name': 'jads',
    'sername': 'put',
}

print(d)
print(
    f'XXXXX #### {a} ---{b}---   {c} list {l} tuple not edit value in tupel {t} : {t[0]}')
print(f'dt is {dt["name"]}')
if dt["name"] == 'jads' and a == 1:
        print(f'{a}')
        print(f'Hello')
elif dt["name"] == 'jadsX':
        print(f'{dt["name"]}')
else: 
        print(f'Else ')

for item in dt:
        if item == "name" :
              print(f'xxxx {item}')
        print(f'--{item}')
print( f'{dt.items()}')
