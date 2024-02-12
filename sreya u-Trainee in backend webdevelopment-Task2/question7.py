# 7.Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow

def hypen_separated_word(sequence):
    words = sequence.split('-')
    sorted_words = sorted(words)
    joined_words = '-'.join(sorted_words)
    return joined_words

input_sequence = input("Enter a hyphen-separated sequence of words: ")
sorted_sequence = hypen_separated_word(input_sequence)
print("Sorted sequence:", sorted_sequence)
