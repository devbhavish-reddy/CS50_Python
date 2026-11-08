def main(): 
    num = int(input("N:"))
    sum_num(num)

def sum_num(a): 
    sum = 0
    while a >  0: 
        sum = sum + (a % 10)
        a = a // 10
    print(sum)



main()