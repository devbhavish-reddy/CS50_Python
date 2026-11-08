"""
Classes: 
    Enables us to create our own data-type in python. 
    It helps to create objects in python. 

The analogy of what happens behind the scenes: 
    self acts as a temporary internal pointer that anchors a class blueprint to an object’s physical memory address during creation. 
    The moment you instantiate a class, Python reserves a blank slot in memory and automatically passes it into __init__ as self. 
    By using dot notation (like self.name), you instruct Python to open that specific memory slot and create isolated sub-variables (attributes) directly inside it.
    Crucially, self operates independently of external code and remains completely unaware of outside variable names like student. Once initialization finishes, self evaporates, 
    and Python passes the keys to that finalized, structured memory slot out to your main variable.
 
"""

class Student: 
    def __init__(self, name, age):
        if not name: 
            raise ValueError("Incomplete Str") #Raise keyword lets the programmer manually raise an issue.  
        self.name = name
        self.age = age      #Instance Varibeles in the working now.


    def __str__(self): 
        return "student is here" 

    



def main(): 
    student = get_student()
    print(f"{student.name} age is {student.age}")

def get_student(): 
    name = input("Enter name: ")
    age = int(input("Age: "))
    return Student(name, age)

if __name__ == "__main__": 
    main()

