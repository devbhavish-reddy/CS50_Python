class Student:

    def __init__(self, name, house): 
        self.name = name
        self.house = house
 

    @classmethod
    def get(cls, name, house): 
        return cls(name, house) 
    




def main(): 
     student = Student.get("Bhavish", "Hercules")
     print(student.name)

if __name__ == "__main__": 
    main()



