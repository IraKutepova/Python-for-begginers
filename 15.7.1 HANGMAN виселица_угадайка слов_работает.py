import random
#word_list = ['fruit', 'human', 'sweater', 'finger', 'circle', 'watch']
word_list = ['дракон', 'динозавр', 'свинья', 'кот', 'бобр', 'хомяк']
#word_completion = '_ ' * len(word)

# выбор слова для игры
def get_word():
    return random.choice(word_list).upper()

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

# check the word
def is_right_word(guess, word):
    flag = False
    #print('hi is_right_word')
    if guess.upper() == word:
        flag = True
    #print(guess, flag)
    return flag


# if letter is right replace '_' to 'b' for example
def is_right_letter(guess, word, word_c):
    
   # print('herer1')
    for i in range(len(word)):
        if guess[i].upper() == word[i]:
            del word_c[i]
            word_c.insert(i, word[i])
            #print('herer', word_c)
    
    return ' '.join(word_c)

# game
def play(word):
    word_completion = '_ ' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток 
    word_c = word_completion.split()
    #word_c = ''
    #print(word)
    print('Давайте играть в угадайку слов! (Загадано слово на русском языке)')
    print(display_hangman(tries))
    print(word_completion)
    while not guessed:
        print(f'Попытайтесь угадать слово. Осталось {tries} попыток.')
        guess = input('Ваше слово: ')
        if guess.isalpha() and len(guess) == len(word):
            #guessed_letters.extend(guess.upper())
            
            #print(guessed_words)
            if is_right_word(guess, word):
                print('Поздравляем, вы угадали слово! Вы победили!')
                guessed = True
                break
            else:
                if guess.upper() not in guessed_words: 
                    guessed_words.append(guess.upper())
                    if tries > 1:
                        tries -= 1
                    else:
                        print(display_hangman(0))
                        print(f'Простите, но вы проиграли. Было загадано слово: {word}. \nCыграем еще? (1 - да, 0 - нет)')
                        ans = int(input())
                        if ans == 0:
                            print('До свиданья!')
                            break
                        else:
                            word = get_word()
                            tries = 6
                      
                print(is_right_letter(guess, word, word_c))
                print(display_hangman(tries))
        else:
            print(f'Введите задуманное слово из {len(word)} букв, без цифр или символов!')  
    

# main body
word = get_word() 

play(word)