# Define a function that accepts lowercase words and returns uppercase words. 

def uppercase_lowercase_word():
    while True:
        word = input("Enter a lowercase word: ")
        if word.islower(): 
            return word.upper()
        else:
            print("Please enter a word in lowercase letters.")

output_word = uppercase_lowercase_word()
print(output_word) 
