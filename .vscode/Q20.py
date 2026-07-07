numbers=[1,2,3,4,5,6]
evens=filter(lambda x: x % 2 != 0 ,numbers)
print("EVEN NUMS IN GIVEN NUMS ARE : ",list(evens))


squares=map(lambda x: x**2 ,numbers)
print("SQUARES OF GIVEN NUMS ARE : ",list(squares))

add=lambda x,y: x+y
sum=add(4,5)
print("SUM : ",sum)