import random
k = 0
c = ''
while k < 4:
    a = random.randint(1, 6)
    if a == 1:
        b = 'А'
    elif a == 2:
        b = 'Е'
    elif a == 3:
        b = 'Н'
    elif a == 4:
        b = 'О'
    elif a == 5:
        b = 'С'
    elif a == 6:
        b = 'Т'
    c = c + b
    k = k + 1
n = 1
print('Загадано четырехбуквенное слово из букв А,E,Н,О,С,Т.')
print('Отгадай!')
s = 0
d = 0
while n < 11 or s == 4:
    print('Попытка №: ', n)
    x = input()
    if x[0] == c[0]:
        s = s + 1
    else:
        d = d + 1
    if x[1] == c[1]:
        s = s + 1
    else:
        d = d + 1
    if x[2] == c[2]:
        s = s + 1
    else:
        d = d + 1
    if x[3] == c[3]:
        s = s + 1
    else:
        d = d + 1
    if s == 4:
        print('Вы выйгрвли!')
        break
    else:
        print('На "своём месте": ', s)
        print('На "чужом месте": ', d)
    s = 0
    d = 0
    n = n + 1