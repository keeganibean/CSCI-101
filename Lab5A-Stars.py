def print_stars(n):
    pyramid = 2*n - 2
    for wordd in range(0, n):
        for stars in range(0, pyramid): 
            print(end=" ")
        pyramid = pyramid - 1
        for stars in range(0, wordd+1):           
            print("* ", end="")
        print("\r")
#print_stars(3)
def print_word(word):
    print_stars(len(word))
    nospace = ""
    for letter in word:
        nospace = nospace + letter + " "
    nospace = nospace[:-1]
    print (((len(word)-1)*' ')+nospace)
#print_word('cat')
def main():
    print_word(str(input('Word:')))
main()        
    
