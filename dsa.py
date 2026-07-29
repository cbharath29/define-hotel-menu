try:
    n = int(input())
    
    if n<0:
        print("error: invalid syntax")
    else:
        cost = 0
        if n <= 2:
            cost = n*100
        elif n<=3:
            cost = 2*200 + (n-n*50)
        elif n<= 5:
            cost = 2*200 + (3*50) + (n-5*20)
        else:
            print("error:invalid syntax")
        print(cost)
except:
    print("Error: Invalid input")