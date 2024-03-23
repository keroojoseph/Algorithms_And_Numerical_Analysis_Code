from math import sqrt
def fun(x):
    return sqrt(x) - x

def bisection(a, b):

    if (fun(a) * fun(b) > 0):
        print("error...!")
        return
    
    c = (a + b) / 2

    while(abs(fun(c)) >= .0001):
        c = (a + b) / 2
        print(f"{a:.4f}  |  {b:.4f}  |  {c:.4f}  |  {fun(c):.6f}")
        print("-------------------------------------------")
        if(fun(a) * fun(c) < 0):
            b = c
        else:
            a = c
    print("the root is: %f" %c)
            
bisection(25, 1)
