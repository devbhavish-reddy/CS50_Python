class Maths: 
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __str__(self): 
        return f"Name is {self.name} and birth year is {self.year}"

    def check(self): 
        match self.name: 
            case "Bhavish":
                return 2010

            case "Chinna": 
                return 2010

            case "kanna": 
                return 2010

            case "Avaneesh": 
                return 1900
            

    

def main(): 
    results = myself()
    print(results)
    print(Maths.check(results))

def myself(): 
    name = input("Name:  ")
    year = int(input("Year: "))
    return Maths(name, year)

if __name__ == "__main__": 
    main()

