def count_vowels(str):
    vowels="aeiouAEIOU"
    count=0
    for char in str:
         if char in vowels:
             count +=1
    print(f"No of vowels in string : {count}")

def reverse_string(str):
    return str[::-1]

def is_palindrome(str):
    str=str.lower()
    return str == str[::-1]
   