# Write a Python program that accepts a hyphen-separated sequence of words as input and prints 
# the words in a hyphen-separated sequence after sorting them alphabetically. 
# Sample Items : green-red-yellow-black-white 
# Expected Result : black-green-red-white-yellow 
def sort_hyphen_separated(sqnce):
    words = sqnce.split('-')
    sorted_words = sorted(words)
    sorted_sequence = '-'.join(sorted_words)
    return sorted_sequence

input_sequence = input("Enter a hyphen-separated sequence of words: ")
sorted_sequence = sort_hyphen_separated(input_sequence)
print("Sorted hyphen-separated sequence:", sorted_sequence)
