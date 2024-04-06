if 3>2:
    print('It works!')
if 5>20:
    print('5 es mayor a dos')
else:
    print('5 no es mayor a dos')
name = 'm.elissa'
if name == 'martin':
    print('holi martin')
elif name == 'm.elissa':
    print('holi m.elissa')
else:
    print('holi stalker!')
def hi():
    print('holi')
    print('que mas!')
def hi(name):
    if name == 'martin':
        print('holi martin')
    elif name == 'm.elissa':
        print('holi m.elissa')
    else:
        print('holi stalker!')
hi('martin')
def hi(name):
    print('holi'+name+'!')
hi('Rachel')
def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'm.elissa']
for name in girls:
    hi(name)
for i in range(0, 19):
    print(i)
