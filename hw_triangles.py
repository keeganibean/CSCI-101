import math
def area(a,b,c):
    s=((a+b+c)/2)
    area=((s*(s-a)*(s-b)*(s-c))**(1/2))
    return area
print ((area(3,4,5)))
def is_heronian(a,b,c):
    if ((a)%1==0) and ((b)%1==0) and ((c)%1==0) and ((area(a,b,c))%1==0):
        print('True')
    else:
        print('False')
is_heronian(3,4,5)
