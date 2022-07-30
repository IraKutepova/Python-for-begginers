from random import randint

def guess():
    left, right = 1, 100
    middle = -1
    num = randint(left, right)
    count = 0
    while middle != num:
        count += 1
        middle = (left + right) // 2
        if middle == num:
            count += 1
        if middle < num:
            left = middle + 1
        if middle > num:
            right = middle - 1
    return count

def guaranteed_check():
    max_att = -1
    for i in range(1000):
        result_guess_func = guess()
        if result_guess_func > max_att:
            max_att = result_guess_func - 1
    print(f"Guaranteed with {max_att} attempts")

guaranteed_check()