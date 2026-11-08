def main( ): 
    construct_brick(4, 3)
    construct_sqaure(4)
    

def construct_brick(n, y): 
    for _ in range(n): 
        print("$" * y)


def construct_sqaure(m): 
    for _ in range(m): 
        print('.' * m)

# Another way

def construct_sqaure2(m): 
    for _ in range(m):
        for _ in range(m): 
            print("x")

construct_sqaure2(4)

main()

















