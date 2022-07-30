# объявление функции
def convert_to_python_case(text):
    str_py = ''
    str1 = text.upper()
    l = []
    l.extend(text)
    #print(l)
    for i in range(len(l) + 1):
        if l[-1 - i] in str1 and l[-1 - i] not in '0123456789':
            l.insert(-1-i,'_')
        #print(l)
    str_py += ''.join(l)
    str_py1 = str_py.lower() 
    return str_py1

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))