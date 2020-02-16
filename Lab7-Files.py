import re
import random
def clean_word(x):
    return re.sub(r'[^a-z\d ]','',str.lower(x))
clean_word("Painter-Wakefield's")

def read_file(yourfile):
    return [clean_word(word) for line in open(yourfile, 'r') for word in line.split()]
d=((read_file("./sample_file.txt")))

def write_file(wordlist,outputfile,wordnumber,start):
    f=open(outputfile,'w')
    random.seed(start)
    newfile=0
    while newfile < wordnumber:
        f.write(random.choice(wordlist))
        f.write(' ')
        newfile=newfile+1
    return
#write_file(d, "./sample_output.txt", 20, 0) in IDLE
    
