def file_one(filename):
    try:
     with open(filename,"r") as file:
        return file.read()
    except FileNotFoundError:
       print(f"File {filename} not found !!")

def file_two(filename,data):
    try:
     with open(filename,"w") as file:
        file.write(data)
    except FileNotFoundError:
       print(f"File {filename} not found !!")

content=file_one("index.txt")
file_two("Write.txt",content)
print(content)
