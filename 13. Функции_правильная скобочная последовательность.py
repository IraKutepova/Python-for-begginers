# объявление функции
def is_correct_bracket(text):
    count_o, count_c = 0, 0
    if len(text) %2 != 0:
        return False
    else:
        if text[0] == ')' or text[-1] == '(':
            return False
        else:
            for c in text:
                if c == '(':
                    count_o += 1
                elif c == ')':
                    count_c += 1   
                if count_c > count_o:
                    break
            #print(count_o, count_c)
            if  count_o != count_c:
                return False
            else:
                return True
            

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))