def is_palindrome(text):
    text=text.lower()
    for char in text:
        if text==text[::-1]:
         return"String is a palindrome"
        else:
           return"String is not a palindrome"
        
print(is_palindrome("Alyla"))

