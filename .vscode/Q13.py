def is_palindrome(text):

   cleaned_text="".join(char for char in text if char.isalnum()).upper()
   if cleaned_text==cleaned_text[::-1]:
         return f"{text} is a palindrome"
   else:
           return f"{text} is not a palindrome"
        
input_text="A man, A plan, a canal, Panama"
print(is_palindrome(input_text))

