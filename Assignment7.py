# 1) Create a function with a default parameter "file" storing the file path
# 2) Open the "file" in append mode
# 3) Use writelines() method to add your roll number, name, and class
# 4) Use readines() method to print your data in the prompt

# Note: Use try...except block with suitable exception class
def file_operation(roll_no, name,stud_class, file="data.txt"):
    try:
        f=open(file,"a")
        f.write(f"{roll_no} , {name} and {stud_class} ")
        f=open(file,"r")
        data=f.read()
        print("Data is: ")
        print(data)

    except FileNotFoundError:
        print(f"{file} was not found....enter correct file name")

    except Exception:
        print("Something went wrong")
file_operation(38, "Dhvani", "3rd Year")
