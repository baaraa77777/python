import random
word_list = ["mouse", "apples", "baboon"]

choosen_word = random.choice(word_list)
print(choosen_word)

guess_letter = input("Guess the letter in a word: ").lower()
for letter in choosen_word:
    if letter == guess_letter:
        print("Right")
    else:
        print("Wrong")