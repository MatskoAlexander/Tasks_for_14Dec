import random
k = 0
guessed = ''
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
    guessed = guessed + b
    k = k + 1
n = 1
print('Загадано четырехбуквенное слово из букв А,E,Н,О,С,Т.')
print('Отгадай!')
s = 0
d = 0
while n <= 10 and s != 4:
    print('Попытка №: ', n)
    answer = input().upper()
    if answer[0] == guessed[0]:
        s = s + 1
    elif answer[0] != guessed[0] and guessed.find(answer[0]) != -1:
        d = d + 1
    else:
        pass
    if answer[1] == guessed[1]:
        s = s + 1
    elif answer[1] != guessed[1] and guessed.find(answer[1]) != -1:
        d = d + 1
    else:
        pass
    if answer[2] == guessed[2]:
        s = s + 1
    elif answer[2] != guessed[2] and guessed.find(answer[2]) != -1:
        d = d + 1
    else:
        pass
    if answer[3] == guessed[3]:
        s = s + 1
    elif answer[3] != guessed[3] and guessed.find(answer[3]) != -1:
        d = d + 1
    else:
        pass
    if s == 4:
        print('Вы выиграли!')
    else:
        print('На \"своём месте\": ', s)
        print('На \"чужом месте\": ', d)
    s = 0
    d = 0
    n = n + 1
    if n == 11 and s != 4:
        print('Вы проиграли!')