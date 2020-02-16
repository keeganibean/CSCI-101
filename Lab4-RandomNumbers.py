def generate(prev_value):
    a = 1103515245
    c = 12345
    m = 2**31
    randomnumber = (a*prev_value + c) % m
    return randomnumber
print (generate(0))
def rand_int(curr_value, lower, upper):
    size=(upper-lower)+1
    curr_value=curr_value%size
    curr_value=curr_value+lower
    return curr_value
def main():
    seed=int(input("YourSeed:"))
    going=True
    while going:
        lower=int(input("lower:"))
        upper=int(input("upper:"))
        if lower>upper:
            print("Incorrect, upper bound must be higher")
        elif lower==upper:
            print("Incorrect, upper bound and lower bound cannot be equal")
        else:
            prev_value=seed
            seed=generate(seed)
            number=rand_int(seed,lower,upper)
            print(number)
        check=input("Continue?")
        if check=="Yes" or check=="Y" or check=="y" or check=="sure":
            going=True
        else:
            going=False
            print("Have a nice day")
    return
main()
