def score(base_1, base_2):
    if base_1==base_2:
        print('+1')
    elif base_1!=base_2:
        print('-1')
    elif (base_1=='-' or base_2=='-'):
        print('-2')
    elif (base_1=='-' and base_2=='-'):
        print('0')
score('A', 'A')
score('A','-')
score('A','G')
