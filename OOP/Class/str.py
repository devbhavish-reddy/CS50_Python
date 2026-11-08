class Str_Object: 
    def __str__(self): 
        return "students present"


def main(): 
     functional = student()
     print(functional)

def student(): 
    return Str_Object()

if __name__ == "__main__": 
    main()
