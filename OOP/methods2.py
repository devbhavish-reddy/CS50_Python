"""
Class Methods: 

    Class methods refer to dealing with a class, where the concerned attribute affects the whole class. 

    ANALOGY: A house blueprint in the neigbourhood may have certain things such as the sewage blue pritn which is common to all the house's
    not the one which belongs to some special person. 

    The purpose of this method is to make the method standalone for the class itself, no matter how many instance variables or objects. 

"""
from random import choice

class Indus: 
    def __init__(self, student):
        self.name = student 
        self.houses = ["Hercules", "Oreon", "Phoenix", "Pegasus"]
         


    # def sort(self, student):
    #     if student == "Sharan": 
    #         print("Hercules")
    def sort(self): 
        print(f"Student is {self.name}, and house is {choice(self.houses)}")
student = Indus("Sharan")
student.sort()