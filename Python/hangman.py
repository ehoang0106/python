import random
from file import word_list

random_word = random.choice(word_list)
word_length = len(random_word)

print(random_word)
array = []

for letter in random_word:
    array += "_"
print(array)

guess = input("guess a letter: ")

for position in range(word_length):
    letter = random_word[position]
    if letter == guess:
        array[position] = letter
print(f"{' '.join(array)}")