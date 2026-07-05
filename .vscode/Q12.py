import re

def clean_text():
    text=input("Enter the text : ")
    text=re.sub(r"[^\w\s]","",text)

    text=" ".join(text.split())
    return text.lower()

cleaned_text=clean_text()
print(cleaned_text)
