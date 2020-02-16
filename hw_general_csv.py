import csv
import os
def read_csv(path):
    if os.path.exists(path) is False:
        print('no')
        return None
    if '.csv' not in path:
        print('no')
        return None
    mylist = []
    with open(path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            mydict={}
            if row['DATE'].isdigit() is True:
                mydict['DATE']=float(row['DATE'])
            else:
                mydict['DATE']=row['DATE']
            if row['PRCP'].isdigit() is True:
                mydict['PRCP']=float(row['PRCP'])
            else:
                mydict['PRCP']=row['PRCP']
            if row['TMAX'].isdigit() is True:
                mydict['TMAX']=float(row['TMAX'])
            else:
                mydict['TMAX']=row['TMAX']
            if row['TMIN'].isdigit() is True:
                mydict['TMIN']=float(row['TMIN'])
            else:
                mydict['TMIN']=row['TMIN']
            if row['RAIN'].isdigit() is True:
                mydict['RAIN']=float(row['RAIN'])
            else:
                mydict['RAIN']=row['RAIN']
            mylist.append(mydict)
        return mylist
rows = read_csv("./seattleWeatherData.csv")
def print_averages(x):
    avgprcp=0
    totalprcp=0
    avgtmax=0
    totaltmax=0
    avgtmin=0
    totaltmin=0
    for row in x:
        avgprcp=avgprcp+float(row['PRCP'])
        totalprcp+=1
        averagePRCP=avgprcp/totalprcp
        avgtmax=avgtmax+float(row['TMAX'])
        totaltmax+=1
        averageTMAX=avgtmax/totaltmax
        avgtmin=avgtmin+float(row['TMIN'])
        totaltmin+=1
        averageTMIN=avgtmin/totaltmin
    print("DATE is non-numeric")
    print("TMAX average =",averageTMAX)
    print("PRCP average =",averagePRCP)
    print("TMIN average =",averageTMIN)
    print("RAIN is non-numeric")
        
            
            

