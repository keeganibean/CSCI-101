def permute(x, count=0):
    if count==len(x):
        print(''.join(x))
    for word in range(count, len(x)):
        mystring=[y for y in x]
        mystring[count],mystring[word]=mystring[word],mystring[count]
        permute(mystring, count=count+1)
permute('ABCD')
