import random
k = 0
lim1 = 0
guessed = ''
letter = 'АЕНОСТ'
while k <= 4:
    a = random.randint(1, 6)
    if a != lim1:
        if a == 1:
            b = letter[0]
        elif a == 2:
            b = letter[1]
        elif a == 3:
            b = letter[2]
        elif a == 4:
            b = letter[3]
        elif a == 5:
            b = letter[4]
        elif a == 6:
            b = letter[5]
        else:
            pass
        guessed = guessed + b
        lim1 = a
        k = k + 1
        if ((guessed.count(letter[0]) > 1) or (guessed.count(letter[1]) > 1) or (guessed.count(letter[2]) > 1
        ) or (guessed.count(letter[3]) > 1) or (guessed.count(letter[4]) > 1) or (guessed.count(letter[5]) > 1)):
            k = 0
            guessed = ''
print('Загадано четырехбуквенное слово из букв А,E,Н,О,С,Т.')
print('Отгадай!')
counter1 = 1
counter2 = 0
true = 0
false = 0
s = ''
while counter1 <= 10 and true != 4:
    print('Попытка №: ', counter1)
    answer = input().upper()
    if len(answer) == 4:
        count2 = 0
        for i in range(4):
            count1 = answer.count(answer[i])
            if answer[i] == guessed[i]:
                true = true + 1
            elif answer[i] != guessed[i] and answer[i] in guessed:
                false = false + 1
                if answer.count(answer[i]) == 4:
                    false = 0
            else:
                pass
            if count1 >= count2:
                count2 = count1
        if count2 == 3 and true == 1:
                if false == 1:
                    false = 0
                elif false > 1:
                    false = 1
        elif count2 == 3 and false == 2 and true == 2:
            false = 0
        elif count2 == 2:
            if true == 3:
                false = 0
            elif true == 2 and false == 2:
                false = 0
        elif count2 == 1:
            if true == 3 and false == 1:
                false = 0
        counter1 = counter1 + 1
        if true == 4:
            print('Вы выиграли!')
            print('На \"своём месте\": ', true)
            print('На \"чужом месте\": ', false)
            break
        elif counter1 == 11 and true != 4:
            print('Вы проиграли!')
            print('На \"своём месте\": ', true)
            print('На \"чужом месте\": ', false)
            print('Загаданное слово: ', guessed)
        else:
            print('На \"своём месте\": ', true)
            print('На \"чужом месте\": ', false)
        true = 0
        false = 0
    else:
        print('Ведите 4 буквы.')
        continue
