def write_to_file(filename,items):
    with open(filename,"w") as file:
        for item in items:
          file.write(item + "\n")

def read_to_file(filename):
   try:
      with open(filename,"r") as file:
         items=file.readlines()

         for item in items:
            print(item.strip())
   except FileNotFoundError:
      print(f"File {filename}  not found !!")

fruits={"Apple","Banana","Dates"}
write_to_file("fruits.txt",fruits)
read_to_file("fruits.txt")