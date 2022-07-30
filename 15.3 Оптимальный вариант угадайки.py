import random
import math
def is_right_number(num2):
    flag = False
    left, right = 1, 100
    count = 0
    while not flag:
        middle = (left + right) // 2
        if middle == num2:
            print('Вы угадали, поздравляем!')
            print(middle, count)
            flag = True
            break
        elif middle > num2:
            print('Слишком много, попробуйте еще раз!')
            right = middle - 1
            count += 1
            
        else:
            print('Слишком мало, попробуйте еще раз!')
            left = middle + 1
            count += 1

def max_count_guess():
    range_guess = 100
    count = math.log(range_guess, 2)
    print(f"Максимальное число попыток для n={range_guess} будет {math.ceil(count)}")

#num1 = int(input())
num2 = random.randint(1,100)
is_right_number(num2)
max_count_guess()