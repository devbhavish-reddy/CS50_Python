from main import square

def main(): 
    for j in range(0,100): 
        test_sqaure(j)



def test_sqaure(n): 
   assert square(n) == n * n 

if __name__ == "__main__": 
    main()





 