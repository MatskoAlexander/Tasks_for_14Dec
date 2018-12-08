text = str(input('Введите текст:\n '))
type_lang = str(input('Введите язык: '))

if type_lang.lower() == 'синий':
    sconsonant = 'c'
elif type_lang.lower() == 'кирпичный':
    sconsonant = 'к'
elif type_lang.lower() == 'фиолетовый':
    sconsonant = 'ф'
elif type_lang.lower() == 'белый':
    sconsonant = 'б'

n = 0
vowels = 'аеёиоуыэюя'
vowels = vowels + vowels.upper()
for i in vowels:
    num = text.find(i, n)
    if num != -1:
        text = text.replace(i, i + sconsonant + i.lower())
        n = n + 1
    else:
        n = 0
print(text)