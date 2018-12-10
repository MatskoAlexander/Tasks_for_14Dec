import random
k = 0
lim1 = 0
guessed = ''
while k < 4:
    a = random.randint(1, 6)
    if a != lim1:
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
        guessed = guessed + b
        lim1 = a
        k = k + 1
n = 1
print('Загадано четырехбуквенное слово из букв А,E,Н,О,С,Т.')
print('Отгадай!')
s = 0
d = 0
lim2 = 0
guessed = 'ЕНОТ'
while n <= 10 and s != 4:
    print('Попытка №: ', n)
    answer = input().upper()
    for i in range(4):
        if answer[i] == guessed[i]:
            s = s + 1
        elif answer[i] in guessed and answer[0] != answer[1] and answer[1] != answer[2] and answer[2] != answer[3]\
                and answer[0] != answer[2] and answer[1] != answer[3]:
            d = d + 1
        elif answer[i] in guessed and guessed.count(answer[i]) >= 1:
            d = 0

    if s == 4:
        print('Вы выиграли!')
        print('На \"своём месте\": ', s)
        print('На \"чужом месте\": ', d)
    else:
        print('На \"своём месте\": ', s)
        print('На \"чужом месте\": ', d)
        s = 0
        d = 0
    n = n + 1
    if n == 11 and s != 4:
        print('Вы проиграли!')
        print('На \"своём месте\": ', s)
        print('На \"чужом месте\": ', d)
