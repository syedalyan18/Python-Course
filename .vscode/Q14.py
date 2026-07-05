sentence=input("Enter the string : ")
words=sentence.split()
rearranged_words=words[::-1]
result=" ".join(rearranged_words)
print(rearranged_words)