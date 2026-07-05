student={"Name":"Anas","Age": 19,"Grade" :"A"}
student["Address"]="NYC"
print(student)
student["Age"]=20
if "Grade" in student:
    del student["Grade"]
print(student)

