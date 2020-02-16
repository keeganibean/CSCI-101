import os
def read_metar(x):
    if os.path.exists(x) is False:
        return None
    if '.txt' not in x:
        return None
    with open('./metar.txt') as f:
        lines = f.readlines()
        mylist=[]
        for line in lines:
            line=line.strip('\n')
            space=line.split(' ')
            mylist.append(space)
    return mylist
def parse_metar(y):
    if y[0]=='METAR':
        print('TYPE: standard')
    if y[0]=='SPECI':
        print('TYPE: special')
    ID=y[1]
    print('ID:',ID)
    time =int(y[2][2:6])-600
    if time>0:
        print('TIME: %04d UTC' %time)
    else:
        print('TIME:',abs(time),'UTC') #Negative Time
    wind=int(y[3][4:5]) #ignore direction and gusts
    print('WIND:',wind,'knots')
    vis=int(y[4][0:-2])
    print('VIS: %d miles' %vis)
    weatherconditions={'-':'Light','+':'Heavy','VC':'In the Vicinity','MI':'Shallow','PR':'Partial','BC':'Patches','DR':'Low Drifting','BL':'Blowing','SH':'Showers','TS':'Thunderstorm','FZ':'Freezing','DZ':'Drizzle','RA':'Rain','SN':'Snow','SG':'Snow Grains','IC':'Ice Crystals','PL':'Ice Pellets','GR':'Hail','GS':'Snow Pellets','UP':'Unknown Precipitation','BR':'Mist','FG':'Fog','FU':'Smoke','VA':'Volcanic Ash','DU':'Widespread Dust','SA':'Sand','HZ':'Haze','PY':'Spray','PO':'Well-Developed Dust/Sand Whirls','SQ':'Squalls','FC':'Funnel Cloud Tornado Waterspout','SS':'Sandstorm'}
    if len(y[5])!=3 and len(y[5])!=5:
        print('WX: none reported')
    elif len(y[5])==3:
        weathertype=y[5][0]
        if weathertype in weatherconditions:
            description=weatherconditions[weathertype]    
        weatherstyle=y[5][1:3]
        if weatherstyle in weatherconditions:
            weather=weatherconditions[weatherstyle]
        print('WX: %s %s' %(description,weather))
    skystuff={'SKC':'Sky Clear','NCD':'Nil Cloud Detected','CLR':'No clouds below 12000 ft','NSC':'No Significant Cloud','FEW':'Few','SCT':'Scattered','BKN':'Broken','OVC':'Overcast','VV':'Clouds cannot be seen'}
    showsky=''
    for part in y:
        if len(part)==6:
            if part[0:3].isalpha and part[3:6].isdigit and part[0:3] in skystuff:
                clouds=skystuff[part[0:3]]
                height=int(part[3:6])*100
                showsky=(showsky+(' '+clouds+' at '+str(height)+' ft'+','))
    print('SKY:',(showsky[0:-1]))
    for metardata in y:
        if '/' in metardata:
            T=(metardata[0:2])
            TD=(metardata[3:5])
    print('T/TD:',T,'Celsius',',','dew point',TD,'Celsius')
lines = read_metar('./metar.txt')
    
