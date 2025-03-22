import random

word_list = ['пекариус', 'бариста', 'выходной', 'доставка', 'фартук']

def get_word():
    return random.choice(word_list).upper()

def display_hangman(tries):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
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

def play(word, player_names):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    current_player = 0

    print('Давайте играть в угадайку слов!')

    print(display_hangman(tries))
    print(word_completion)
    print()

    while not guessed and tries > 0:
        print(f"Теперь ходит {player_names[current_player]}:")
        guess = input('Введите букву или слово целиком: ').upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('Вы уже называли букву', guess)
            elif guess not in word:
                print('Буквы', guess, 'нет в слове.')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('Отличная работа, буква', guess, 'присутствует в слове!')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i in range(len(word)) if word[i] == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('Вы уже называли слово', guess)
            elif guess != word:
                print('Слово', guess, 'не является верным.')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Введите букву или слово.')

        print(display_hangman(tries))
        print(word_completion)
        print()

        # Если игрок угадал слово, он продолжает ходить
        if not guessed:
            current_player = 1 - current_player  # Переключение игроков

    if guessed:
        print(f'Поздравляем, игрок {player_names[current_player]} угадал слово! Ты че за  тигрица усатая')
    else:
        print('Вы не угадали слово. Загаданным словом было ' + word + '. Эх лопушки жи ес')

# Ввод имен игроков
player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
player_names = [player1, player2]

again = 'д'

while again.lower() == 'д':
    word = get_word()
    play(word, player_names)
    again = input('Играем еще раз? (д = да, н = нет): ')
