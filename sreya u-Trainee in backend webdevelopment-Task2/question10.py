# 10.Define a function that accepts lowercase words and returns uppercase words.

def uppercase_word(word):
    return word.upper()

lowercase_word = input("Enter a lowercase word: ")
uppercase = uppercase_word(lowercase_word)
print("Uppercase word:", uppercase)
