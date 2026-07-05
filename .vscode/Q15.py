import re

text = input("Enter a text: ")

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

new_text = re.sub(pattern, "[EMAIL REMOVED]", text)

print("\nOriginal Text:")
print(text)

print("\nModified Text:")
print(new_text)