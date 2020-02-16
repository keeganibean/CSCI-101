def rainfall():
    count=0
    num = float(input('Number:'))
    num_sum = 0
    Number=float(num)
    while True:
        Number1=float(num)
        num_sum+=(Number1)
        if float(num)==-9999:
            break
        num = float(input('Number:'))
        if float(num)<0 and float(num) !=-9999:
            num = (num + (abs(num)))
            count=(count-1)
        count=(count+1)
    if count<2:
        print('There needs to be numbers to average')
    else:
        print ((num_sum+9999)/(count))
rainfall()
