def find_factorial(a):
    fact=1
    for i in range(1, a+1):
         fact*=i
    print("Factorial of ",a," is ",fact)

def display(a):
     find_factorial(a)
    
display(6)