numbers = list(map(int, input("Enter list elements separated by space: ").split()))

# Reverse the list
reversed_list = numbers[::-1]

# Remove duplicates
unique_list = list(set(reversed_list))

# Display results
print("Original List:", numbers)
print("Reversed List:", reversed_list)
print("List after removing duplicates:", unique_list)
 