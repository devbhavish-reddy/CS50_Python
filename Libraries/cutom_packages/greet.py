while True:

    try: 
        name = input("Enter Name: ")
        break

    except ValueError:
        pass
     
        


def main():
    hello(name)
    bye(name)

def hello(name__org):
    print(f"Hello, {name__org}") 


def bye(name_org): 
    print(f"Goodbye, {name_org}")

main()

