
def count_word(filename, word):
    with open(filename, "r") as file:
        content = file.read().lower()   
        words = content.split()         
        return words.count(word.lower())

filename = input("Enter file name: ")
word = input("Enter the word to count: ")

count = count_word(filename, word)

print("The word", word, "appears", count, "times.")
