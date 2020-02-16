import random
def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

def plant_power(string1):
    p=random.randint(1,11)
    q=random.randint(1,11)
    r=random.randint(1,11)
    sum=0
    for char in string1:
        if char=='p':
            sum=sum+(factorial(p))
        if char=='q':
            sum=sum+(factorial(q))
        if char=='r':
            sum=sum+(factorial(r))
    return sum

def zombie_power(string2):
    x=random.randint(1,11)
    y=random.randint(1,11)
    z=random.randint(1,11)
    sum1=0
    for char1 in string2:
        if char1=='x':
            sum1=sum1+factorial(x)
        if char1=='y':
            sum1=sum1+factorial(y)
        if char1=='z':
            sum1=sum1+factorial(z)
    return(sum1)
    
def battle(seednumber,firststring,secondstring):
    random.seed(seednumber)
    plant=plant_power(firststring)
    zombie=zombie_power(secondstring)
    print('Plant Power:', plant)
    print('Zombie Power:', zombie)
    if plant>zombie:
        print('Plants save the say!')
    if plant<zombie:
        print('Zombies Conquer!')
    if plant==zombie:
        print('Its a Draw!')
battle(0,'pqr','xyz')

