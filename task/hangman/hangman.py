import random
import sys

words = ['python', 'java', 'kotlin', 'javascript']
task = random.choice(words)
puzzle = len(task) * '-'
symbols = '!?.-_+=~ @*,0123456789][}{#$%&()`<>"|\\\'/;:^'
j = 9
typed = []


def is_ascii(s):
    return all(ord(c) < 128 for c in s)


print("H A N G M A N")
print('Type "play" to play the game, "exit" to quit:')
endgame = input()
while endgame == "play" or "exit":
    if endgame == "exit":
        sys.exit()
    elif endgame == "play":
        break
    else:
        print('Type "play" to play the game, "exit" to quit:')
        endgame = input()


while j > 0:
    if puzzle == task:
        print(f"You guessed the word {puzzle}!\nYou survived!")
        print()
        print('Type "play" to play the game, "exit" to quit:')
        endgame = input()
        if endgame == "play":
            task = random.choice(words)
            puzzle = len(task) * '-'
            continue
        else:
            break
    if j == 1:
        print("You are hanged!")
        print()
        print('Type "play" to play the game, "exit" to quit:')
        endgame = input()
        if endgame == "play":
            task = random.choice(words)
            puzzle = len(task) * '-'
            continue
        else:
            break
    print()
    print(puzzle)
    letter = input("Input a letter: ")
    if len(letter) > 1:
        print("You should input a single letter")
        continue
    if letter in typed:
        print("You already typed this letter")
        continue
    typed.append(letter)
    if letter in task:
        for i in range(len(task)):
            if letter == task[i]:
                temp = list(puzzle)
                temp[i] = letter
                puzzle = "".join(temp)
    elif letter in symbols or not is_ascii(letter) or letter.isupper():
        print('It is not an ASCII lowercase letter')
    elif letter not in task:
        j -= 1
        print("No such letter in the word")
