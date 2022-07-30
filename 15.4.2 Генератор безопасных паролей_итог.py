import random

# КОНСТАНТЫ
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
    
def generator_password(len_password):
    print('Включать ли цифры 0123456789? (да, нет)')
    flag_digit = input()
    print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да, нет)')
    flag_up_alpha = input()
    print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (да, нет)')
    flag_low_alpha = input()
    print('Включать ли символы !#$%&*+-=?@^_ ? (да, нет)')
    flag_symbols = input()
    print('Исключать ли неоднозначные символы il1Lo0O ? (да, нет)')
    flag_same_symbols = input()    
    
    lists, char = [], ''
    if flag_digit.lower() == 'да':
        lists +=  digits
    if flag_up_alpha.lower() == 'да':
        lists +=  uppercase_letters
    if flag_low_alpha.lower() == 'да':
        lists +=  lowercase_letters            
    if flag_symbols.lower() == 'да':
        lists +=  punctuation     
    if flag_digit.lower() == 'нет' and flag_up_alpha.lower() == 'нет' and flag_low_alpha.lower() == 'нет' and flag_symbols.lower() == 'нет':
        print('Пароль не может быть пуст, создадим буквенный пароль')
        lists +=  lowercase_letters
    
    if flag_same_symbols.lower() == 'да':
        lists1 = []
        for i in range(len(lists)):
            if lists[i] not in 'il1Lo0O':
                lists1.append(lists[i])
            else:
                continue
        lists = lists1
    #print(lists1)
    random.shuffle(lists)
    flag = False
    for i in range(len_password):
        char += random.choice(lists)
    return char
    
print('Cколько паролей необходимо сгенерировать?')
count_passwords = int(input())
print('Длина одного пароля?')
len_password = int(input())

for i in range(count_passwords):
    chars = generator_password(len_password) 
    print('Сгенерированный пароль:', chars)
    if count_passwords > 1:
        print('Следующий пароль:')