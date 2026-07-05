# grades={"Ali" : 75,"Anas" : 84,"Tahir" : 91}
# sum = grades["Ali"] + grades["Anas"] + grades["Tahir"]
# print("AVERAGE GRADE :",sum/3)


n=int(input("Enter th no of Students : "))

students={}

for i in range(n):
    name=input("Enter the name os Student : ")
    grade=float(input("Enter the grade of Student : "))
    students[name]=grade

print("Student Grades:")
for name, grade in students.items():
    print(name, ":", grade)

total = sum(students.values())
avg=total/len(students)
print("\nAVERAGE GRADE : ",avg)