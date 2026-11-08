"""

Properties: 
    Special attributes which boost the defense mechanism of some given code. It ensures that the code
    cannot be modified by everyone and anyone. 

Decorators: 
    Functions which help to modify other functions. 

    
Setter and Getter. 

    Setter: 
        The setter functions deals with setting the instance variable or assigning it to a new value. 

    Getter: 
        The Getter function is like a security gate. It checks if your are authorized to change instance variables. 

    Encapsulation: 
        Encapsulation means bundling data and the methods that operate on that data inside a class, 
        while controlling how that data is accessed or modified.


 
 
 """


std = ["Bhavish", "Kanna", "Chinna", "Abhiram", "Ubaidh"]

class Student: 
    def __init__(self, name, age):  
        self.name = name
        self.age = age      #Instance Varibeles in the working now.


    def __str__(self): 
        ...
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name not in std: 
            raise ValueError('Name not in list.')
        self._name = name

    @property
    def age(self): 
        return self._age


    @age.setter
    def age(self, new_age): 
        if not new_age: 
            raise ValueError
        self._age = new_age


      
def main(): 
    student = get_student()   
    student.name = input("New Record:  ")
    student.age = input("New Age:  ")
    print(f"{student.name} age is {student.age}")


def get_student(): 
    name = input("Enter name: ")
    age = int(input("Age: "))
    return Student(name, age)

if __name__ == "__main__": 
    main()




