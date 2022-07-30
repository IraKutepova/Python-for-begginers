import random

def is_valid_name(name):
    if name.isalpha():
        return True
    else:
        return False

def intro_game():
    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
    print('Как тебя зовут?')
    name = input()
    flag = True
    while flag:
        if is_valid_name(name):
            print('Привет,', name)    
            flag = False
            break
        else:
            print('Введите имя')
            name = input()
        
def magicball_game(answers):
    flag = True
    while flag:
        print('Какой вопрос вас интересует?')
        question = input()
        print(random.choice(answers))
        print('Остались вопросы? (д - да, н - нет)')
        exit = input()
        if exit.lower() == 'н':
            print('Возвращайся, если возникнут вопросы!')
            flag = False
            break
        else:
            continue
    
       

positive_list = ['Бесспорно','Предрешено','Никаких сомнений','Определенно да','Можешь быть уверен в этом']
not_sure_pos_list = ['Мне кажется - да','Вероятнее всего','Хорошие перспективы','Знаки говорят - да','Да']
negative_list = ['Даже не думай','Мой ответ - нет','По моим данным - нет','Перспективы не очень хорошие','Весьма сомнительно']
neutral_list = ['Пока неясно, попробуй снова','Спроси позже','Сейчас нельзя предсказать','Лучше не рассказывать','Сконцентрируйся и спроси опять']
answers = positive_list + not_sure_pos_list + negative_list + neutral_list
#print(*answers)
intro_game()
magicball_game(answers)