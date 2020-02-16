userword=(str(input('Word:')))
letteramount=1
for letter in range(1, len(userword)+1):
    if letter == len(userword):
        print(userword[letter-1] + str(letteramount), end="")
        break
    elif userword[letter-1] == userword[letter]:
            letteramount+=1
    else:
            print(userword[letter-1] + str(letteramount), end="")
            letteramount=1
