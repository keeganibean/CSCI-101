def plus_silent(x,y):
    try:
        x+y
        print(x+y)
    except:
        pass
def plus_custom(a,b):
    try:
        a+b
        print(a+b)
    except:
        raise TypeError("You can't do that!")
