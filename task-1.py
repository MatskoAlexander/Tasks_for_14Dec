text = input('Введите текст:\n')
type_lang = input('Введите язык: ')

if type_lang.lower() == 'синий':
    sconsonant = 'c'
elif type_lang.lower() == 'кирпичный':
    sconsonant = 'к'
elif type_lang.lower() == 'фиолетовый':
    sconsonant = 'ф'
elif type_lang.lower() == 'белый':
    sconsonant = 'б'
elif type_lang.lower() == 'зелёный':
    sconsonant = 'з'

vowels = 'аеёиоуыэюя'
vowels = vowels + vowels.upper()
for i in vowels:
    text = text.replace(i, i + sconsonant + i.lower())
print(text)