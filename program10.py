# Define a function that accepts lowercase words and returns uppercase words. 

def lowercase_to_uppercase(word):
    return word.upper()

lowercase_word = input("Enter a lowercase word: ")
uppercase_word = lowercase_to_uppercase(lowercase_word)
print(f"Uppercase word: {uppercase_word}")
