# 15.5 Шифр Цезаря кодирование со сдвигом на длину слова
alpha_en = 'abcdefghijklmnopqrstuvwxyz'
# шифрование
def code_Cezar(h, text_):
    text_Cezar = ''
    alphabet = alpha_en
    for c in text_:
        if c in ',./!?"\' -:;+=':
            text_Cezar += c
        elif c in alphabet:
            ind = alphabet.find(c)
            if ind + h > len(alphabet) - 1 :
                h1 = -len(alphabet) + h 
                text_Cezar += alphabet[ind + h1]            
            else:
                text_Cezar += alphabet[ind + h]            
        elif c in alphabet.upper():
            ind = alphabet.upper().find(c)
            if (ind + h) > (len(alphabet) - 1):
                h1 = -len(alphabet) + h 
                text_Cezar += alphabet.upper()[ind + h1]            
            else:
                text_Cezar += alphabet.upper()[ind + h]             
    return text_Cezar

text_tr = input()
words = text_tr.split()
coded = []

for word in words:
    h = 0
    for c in word:
        if c not in '.,-+="!?\'':
            h += 1
    coded.append(code_Cezar(h, word))
print(' '.join(coded))
