import random
from mod import logo, stages
from word import word_list
Game_life = 6
print(logo)



word_guess = random.choice(word_list).lower()
print(word_guess)
display = []
word_len = len(word_guess)


def str_co(disp):
    word = ""
    for _ in disp:
        word += _
    return word


for _ in range(word_len):
    display += "_"
game = True
while game:
    guess = input("Make a guess: ").lower()
    change = True
    for _ in range(word_len):
        letter = word_guess[_]
        if letter == guess:
            display[_] = letter
            change = False
    if change:
        Game_life -= 1
        if Game_life == 0:
            print("You lost")
            game = False
    if "_" not in display:
        print("You won")
        game = False
    print(stages[Game_life])
    print(str_co(display))
