from random import choice

class Students: 
    houses = ["Hercules", "Oreon", "Pegasus", "Phoenix"]

    @classmethod
    def random_bring(cls,name): 
        print(f"Name is {name} from {choice(cls.houses)}")

if __name__ == "__main__":
    Students.random_bring("Bhavish")