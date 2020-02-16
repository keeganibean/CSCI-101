import os
import csv
import csv
print('The dogs names are Kramer, Yoda, and Simba')
from random import randint
def dogsteps(seed):
    a = 1103515245
    c = 12345
    m = 2**31
    randomnumber = ((a*seed + c) % m)/10
    if 0<randomnumber<2800: 
        return int(randomnumber)
    else:
        print(randint(0,2800))
with open('DogAnarchy.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('dogs.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        kramerdict = {rows[0]:rows[1] for rows in reader}
import csv
with open('DogAnarchy.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('dogs.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        yodadict = {rows[2]:rows[3] for rows in reader}
with open('DogAnarchy.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('dogs.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        simbadict = {rows[4]:rows[5] for rows in reader}
dog=input("Which Dog?:")
if dog=='Kramer':
    kramertime=input("Time?:")
    if kramertime=='0:00':
        print('Kramer is',kramerdict['0:00'])
    elif kramertime=='1:00':
        print('Kramer is',kramerdict['1:00'])
    elif kramertime=='2:00':
        print('Kramer is',kramerdict['2:00'])
    elif kramertime=='3:00':
        print('Kramer is',kramerdict['3:00'])
    elif kramertime=='4:00':
        print('Kramer is',kramerdict['3:00'])
    elif kramertime=='5:00':
        print('Kramer is',kramerdict['5:00'])
    elif kramertime=='6:00':
        print('Kramer is',kramerdict['7:00'])
    elif kramertime=='8:00':
        print('Kramer is',kramerdict['8:00'])
    elif kramertime=='9:00':
        print('Kramer is',kramerdict['9:00'])
    elif kramertime=='10:00':
        print('Kramer is',kramerdict['10:00'])
    elif kramertime=='11:00':
        print('Kramer is',kramerdict['11:00'])
    elif kramertime=='12:00':
        print('Kramer is',kramerdict['12:00'])
    elif kramertime=='13:00':
        print('Kramer is',kramerdict['13:00'])
    elif kramertime=='14:00':
        print('Kramer is',kramerdict['14:00'])
    elif kramertime=='15:00':
        print('Kramer is',kramerdict['15:00'])
    elif kramertime=='16:00':
        print('Kramer is',kramerdict['16:00'])
    elif kramertime=='17:00':
        print('Kramer is',kramerdict['17:00'])
    elif kramertime=='18:00':
        print('Kramer is',kramerdict['18:00'])
    elif kramertime=='19:00':
        print('Kramer is',kramerdict['19:00'])
    elif kramertime=='20:00':
        print('Kramer is',kramerdict['20:00'])
    elif kramertime=='21:00':
        print('Kramer is',kramerdict['21:00'])
    elif kramertime=='22:00':
        print('Kramer is',kramerdict['22:00'])
    elif kramertime=='23:00':
        print('Kramer is',kramerdict['23:00'])
    else:
        print('Time must be in military time in the form of 0:00 through 23:00')
    steps=input('Do you want to know how may steps Kramer took yesterday?:')
    if steps=='Yes' or steps=='sure' or steps=='y' or steps=='yes':
        print('Kramer took',dogsteps(0),'steps yesterday')
    else:
        print('Ok have a nice day!')
elif dog=='Yoda':
    yodatime=input("Time?:")
    if yodatime=='0:00':
        print('Yoda is',yodadict['0:00'])
    elif yodatime=='1:00':
        print('Yoda is',yodadict['1:00'])
    elif yodatime=='2:00':
        print('Yoda is',yodadict['2:00'])
    elif yodatime=='3:00':
        print('Yoda is',yodadict['3:00'])
    elif yodatime=='4:00':
        print('Yoda is',yodadict['3:00'])
    elif yodatime=='5:00':
        print('Yoda is',yodadict['5:00'])
    elif yodatime=='6:00':
        print('Yoda is',yodadict['7:00'])
    elif yodatime=='8:00':
        print('Yoda is',yodadict['8:00'])
    elif yodatime=='9:00':
        print('Yoda is',yodadict['9:00'])
    elif yodatime=='10:00':
        print('Yoda is',yodadict['10:00'])
    elif yodatime=='11:00':
        print('Yoda is',yodadict['11:00'])
    elif yodatime=='12:00':
        print('Yoda is',yodadict['12:00'])
    elif yodatime=='13:00':
        print('Yoda is',yodadict['13:00'])
    elif yodatime=='14:00':
        print('Yoda is',yodadict['14:00'])
    elif yodatime=='15:00':
        print('Yoda is',yodadict['15:00'])
    elif yodatime=='16:00':
        print('Yoda is',yodadict['16:00'])
    elif yodatime=='17:00':
        print('Yoda is',yodadict['17:00'])
    elif yodatime=='18:00':
        print('Yoda is',yodadict['18:00'])
    elif yodatime=='19:00':
        print('Yoda is',yodadict['19:00'])
    elif yodatime=='20:00':
        print('Yoda is',yodadict['20:00'])
    elif yodatime=='21:00':
        print('Yoda is',yodadict['21:00'])
    elif yodatime=='22:00':
        print('Yoda is',yodadict['22:00'])
    elif yodatime=='23:00':
        print('Yoda is',yodadict['23:00'])
    else:
        print('Time must be in military time in the form of 0:00 through 23:00')
    steps=input('Do you want to know how may steps Yoda took yesterday?:')
    if steps=='Yes' or steps=='sure' or steps=='y' or steps=='yes':
        print('Yoda took',dogsteps(0),'steps yesterday')
        if dogsteps(0)>1000:
            print('yay')
        else:
            print('no')
    else:
        print('Ok have a nice day!')
elif dog=='Simba':
    time=input("Time?:")
    if time=='0:00':
        print('Simba is',simbadict['0:00'])
    elif time=='1:00':
        print('Simba is',simbadict['1:00'])
    elif time=='2:00':
        print('Simba is',simbadict['2:00'])
    elif time=='3:00':
        print('Simba is',simbadict['3:00'])
    elif time=='4:00':
        print('Simba is',simbadict['3:00'])
    elif time=='5:00':
        print('Simba is',simbadict['5:00'])
    elif time=='6:00':
        print('Simba is',simbadict['7:00'])
    elif time=='8:00':
        print('Simba is',simbadict['8:00'])
    elif time=='9:00':
        print('Simba is',simbadict['9:00'])
    elif time=='10:00':
        print('Simba is',simbadict['10:00'])
    elif time=='11:00':
        print('Simba is',simbadict['11:00'])
    elif time=='12:00':
        print('Simba is',simbadict['12:00'])
    elif time=='13:00':
        print('Simba is',simbadict['13:00'])
    elif time=='14:00':
        print('Simba is',simbadict['14:00'])
    elif time=='15:00':
        print('Simba is',simbadict['15:00'])
    elif time=='16:00':
        print('Simba is',simbadict['16:00'])
    elif time=='17:00':
        print('Simba is',simbadict['17:00'])
    elif time=='18:00':
        print('Simba is',simbadict['18:00'])
    elif time=='19:00':
        print('Simba is',simbadict['19:00'])
    elif time=='20:00':
        print('Simba is',simbadict['20:00'])
    elif time=='21:00':
        print('Simba is',simbadict['21:00'])
    elif time=='22:00':
        print('Simba is',simbadict['22:00'])
    elif time=='23:00':
        print('Simba is',simbadict['23:00'])
    else:
        print('Time must be in military time in the form of 0:00 through 23:00')
    steps=input('Do you want to know how may steps Simba took yesterday?:')
    if steps=='Yes' or steps=='sure' or steps=='y' or steps=='yes':
        simbasteps='Simba took'
        step3='steps'
        print('Simba took',dogsteps(0),'steps yesterday')
    else:
        print('Ok have a nice day!')
else:
    print('Must use the dog names given earlier')
        

