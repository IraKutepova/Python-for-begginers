import random

def is_right_number(num1, num2):
    flag = False
    count = 0
    while not flag:
        
              
        if num1 == num2:
            print('Вы угадали, поздравляем!')
            print(num1)
            flag = True
            break
        elif num1 > num2:
            print('Слишком много, попробуйте еще раз!')
            count += 1
            num1 = int(input())
            
        else:
            print('Слишком мало, попробуйте еще раз!')
            count += 1
            num1 = int(input())
                        


num2 = random.randint(1,100)
print('Добро пожаловать в числовую угадайку')
num1 = int(input()) 
is_right_number(num1, num2)
