import string
import sys
import time
import random
from words import words
word = random.choice(words)  # randomly chooses something from the list
while '-' in word or ' ' in word:
    word = random.choice(words)
#splitting the word
#hiding the data
list_hide = []
for i in word:
    list_hide.append("- ")
#print(word)
list_word = []
for i in word:
    list_word.append(i.lower())
#print(list_word)
def main():
    lim = 0    
    while lim < 10:
        guess = input("Enter a letter: ").lower()
        for letter in list_word:
            count = list_word.count(letter)
            if letter == guess and count == 1:
                index = list_word.index(letter)
                list_hide[index] = letter
                print(list_hide)
                break
            elif letter == guess and count == 2:
                index = list_word.index(letter)
                list_hide[index] = letter
                a = index + 1
                index_1 = list_word[a:].index(letter)
                index_2 = a + index_1
                list_hide[index_2] = letter
                print(list_hide)
                break
            elif letter == guess and count == 3:
                index = list_word.index(letter)
                list_hide[index] = letter
                a = index + 1
                index_1 = list_word[a:].index(letter)
                index_2 = a + index_1
                list_hide[index_2] = letter
                b = index_2 + 1
                index_3 = list_word[b:].index(letter)
                c = b + index_3
                list_hide[c] = letter
                print(list_hide)
                break
            elif letter == guess and count == 4:
                index = list_word.index(letter)
                list_hide[index] = letter
                a = index + 1
                index_1 = list_word[a:].index(letter)
                index_2 = a + index_1
                list_hide[index_2] = letter
                b = index_2 + 1
                index_3 = list_word[b:].index(letter)
                c = b + index_3
                list_hide[c] = letter
                d = c + 1
                index_4 = list_word[d:].index(letter)
                e = d + index_4
                list_hide[e] = letter
                print(list_hide)
                break
            elif letter == guess and count == 5:
                index = list_word.index(letter)
                list_hide[index] = letter
                a = index + 1
                index_1 = list_word[a:].index(letter)
                index_2 = a + index_1
                list_hide[index_2] = letter
                b = index_2 + 1
                index_3 = list_word[b:].index(letter)
                c = b + index_3
                list_hide[c] = letter
                d = c + 1
                index_4 = list_word[d:].index(letter)
                e = d + index_4
                list_hide[e] = letter
                f = e + 1
                index_5 = list_word[f:].index(letter)
                g = index_5 + f
                list_hide[g] = letter
                print(list_hide)
                break
            elif letter == guess and count == 6:
                index = list_word.index(letter)
                list_hide[index] = letter
                a = index + 1
                index_1 = list_word[a:].index(letter)
                index_2 = a + index_1
                list_hide[index_2] = letter
                b = index_2 + 1
                index_3 = list_word[b:].index(letter)
                c = b + index_3
                list_hide[c] = letter
                d = c + 1
                index_4 = list_word[d:].index(letter)
                e = d + index_4
                list_hide[e] = letter
                f = e + 1
                index_5 = list_word[f:].index(letter)
                g = index_5 + f
                list_hide[g] = letter
                h = g + 1
                index_6 = list_word[h:].index(letter)
                i = index_6 + h
                list_hide[i] = letter
                print(list_hide)
                break
            elif letter == guess and count == 7:
                index = list_word.index(letter)
                list_hide[index] = letter
                a = index + 1
                index_1 = list_word[a:].index(letter)
                index_2 = a + index_1
                list_hide[index_2] = letter
                b = index_2 + 1
                index_3 = list_word[b:].index(letter)
                c = b + index_3
                list_hide[c] = letter
                d = c + 1
                index_4 = list_word[d:].index(letter)
                e = d + index_4
                list_hide[e] = letter
                f = e + 1
                index_5 = list_word[f:].index(letter)
                g = index_5 + f
                list_hide[g] = letter
                h = g + 1
                index_6 = list_word[h:].index(letter)
                i = index_6 + h
                list_hide[i] = letter
                j = i + 1
                index_7 = list_word[j:].index(letter)
                k = index_7 + j
                list_hide[k] = letter
                print(list_hide)
                break
            elif letter == guess and count == 8:
                index = list_word.index(letter)
                list_hide[index] = letter
                a = index + 1
                index_1 = list_word[a:].index(letter)
                index_2 = a + index_1
                list_hide[index_2] = letter
                b = index_2 + 1
                index_3 = list_word[b:].index(letter)
                c = b + index_3
                list_hide[c] = letter
                d = c + 1
                index_4 = list_word[d:].index(letter)
                e = d + index_4
                list_hide[e] = letter
                f = e + 1
                index_5 = list_word[f:].index(letter)
                g = index_5 + f
                list_hide[g] = letter
                h = g + 1
                index_6 = list_word[h:].index(letter)
                i = index_6 + h
                list_hide[i] = letter
                j = i + 1
                index_7 = list_word[j:].index(letter)
                k = index_7 + j
                list_hide[k] = letter
                m = k + 1
                index_8 = list_word[m:].index(letter)
                n = index_8 + m
                list_hide[n] = letter
                print(list_hide)
                break  
            else:
                continue

        if list_hide == list_word:
            print("Congrates! You win")
            new = ''
            for x in list_hide:
                new += x 
            print(f"Your Guessed word: {new}")
            print(f"Actual word: {word}")
            break
        lim += 1
    else:
        print("Sorry! You ran out of chances.") 
        print(f"Your Guessed word is wrong!")
        print(f"Actual word: {word}")

print("#############################")
print("WELCOME TO THIS HANGMAN GAME")
print(" Dev By Rakibul Hasan Asif")
print("#############################")
time.sleep(2)
try:
    name = input("Enter Your Name: ")
except ValueError:
    print("Invalid letter!")
except KeyboardInterrupt:
    print(" ")
    print("Sorry! Keyboard Interrupted!")
    sys.exit()

def all():
    try:    
        print(f"Welcome {name}")
        print("Wait!Game is loading....")
        time.sleep(3)
        print(list_hide)
        main()
    except ValueError:
        print("Invalid letter!")
    except KeyboardInterrupt:
        print(" ")
        print("Sorry! Keyboard Interrupted!")
        sys.exit()
all()
try:
    while True:
        choice = input("Do you want to play again?(y or n): ")
        if choice == 'y':
            word = random.choice(words)  # randomly chooses something from the list
            while '-' in word or ' ' in word:
                word = random.choice(words)
            #splitting the word
            #hiding the data
            list_hide = []
            for i in word:
                list_hide.append("- ")
            #print(word)
            list_word = []
            for i in word:
                list_word.append(i.lower())
            all()
            
        elif choice == 'n':
            print("Thanks for Playing. See you soon!")
            sys.exit()
        else:
            print("Invalid choice!")
            sys.exit()
except ValueError:
    print("Invalid letter!")
    sys.exit()
except KeyboardInterrupt:
    print(" ")
    print("Sorry! Keyboard Interrupted!")
    sys.exit()