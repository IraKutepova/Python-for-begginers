# объявление функции
def is_palindrom(text):
    str = text.lower()
    ls = []
    ls.extend(str)
    str1 = ''
    for i in range(len(ls)):
        if ls[i] not in ' ,.!?-':
            str1 += ls[i]
    flag = True
    for i in range(len(str1) // 2 + 1):
        if str1[i] != str1[-1-i]:
            flag = False
            break
    
    return flag    

def is_prime(num):
    if num <= 1: 
        return False
    else:
        count = 0
        for i in range(2, num + 1):
            if num % i == 0:
                count += 1
        if count == 1:
            return True
        else:
            return False

def is_even(num):
    if num %2 == 0:
        return True
    else:
        return False
        
def is_valid_password(password):
    flag = False
    ls = []
    ls = password.split(':')
    if len(ls) > 3:
        return False
    else:
        a, b, c = ls[0], ls[1], ls[2]
        if is_palindrom(a):
            if is_prime(int(b)):
                if is_even(int(c)):
                    flag = True
    return flag

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))