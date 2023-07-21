import random
import time

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

def is_valid(answer):
    while True:
        if answer not in ('yes', 'no'):
            print('Ответ должен быть "yes" или "no", введите пожалуйста верный ответ:)')    
            time.sleep(5)
        elif answer in ('yes', 'no'):
            break
    return answer

pas_quantity = int(input('Какое количество паролей потребуется?: '))
pas_len = int(input('Сколько символов должно быть в пароле?: '))
pas_numbers = input('Добавить в пароль цифры? Ответ "yes" или "no": ')
is_valid(pas_numbers)
pas_upper_char = input('Добавить в пароль заглавные буквы? Ответ "yes" или "no": ')
pas_lower_char = input('Добавить в пароль строчные буквы? Ответ "yes" или "no": ')
pas_symbol = input('Добавить в пароль символы? Ответ "yes" или "no"?: ')
pas_expectatio = input('Исключать ли неоднозначные символы "il1Lo0O"? Ответ "yes" или "no" ')


if pas_numbers == 'yes':
    chars += digits
if pas_upper_char == 'yes':
    chars += uppercase_letters
if pas_lower_char == 'yes':
    chars += lowercase_letters
if pas_symbol == 'yes':
    chars += punctuation
if pas_expectatio == 'yes':
    for c in 'il1Lo0O':
        chars.replace(c, random.choice(chars))
        
def generate_password(lenght, chars):
        return random.sample(chars, lenght)
for i in range(pas_quantity):
    print(*generate_password(pas_len,chars), sep='')
    
    

    



