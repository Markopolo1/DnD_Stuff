import random



def difficultySet():
    while True:
        encDifficulty=0
        print('How difficult will this challenge be? Easy:[1] Medium:[2] Hard:[3] Deadly:[4]?')
        encDifficulty=input()
        encDifficulty= int(encDifficulty)
        if encDifficulty < 1:
            print('You must enter a valid difficulty.')
        if encDifficulty > 4:
            print('You must enter a valid difficulty.')
        else:
            return(encDifficulty)
            break


def xpEasy(level,count):
    xp=0
    level=int(level)
    count=int(count)
    if level == 1:
        xp=25
    if level == 2:
        xp=50
    if level == 3:
        xp=75
    if level == 4:
        xp=125
    if level ==5:
        xp=250
    if level ==6:
        xp=300
    if level ==7:
        xp=350
    if level ==8:
        xp=450
    if level ==9:
        xp=550
    if level ==10:
        xp=600
    if level == 11:
        xp=800
    if level == 12:
        xp=1000
    if level ==13:
        xp=1100
    if level ==14:
        xp=1250
    if level == 15:
        xp=1400
    if level == 16:
        xp=1600
    if level ==17:
        xp=2000
    if level == 18:
        xp=2100
    if level == 19:
        xp= 2400
    if level == 20:
        xp=2800
    xpThreshold = (xp*count)
    return xpThreshold




def xpMedium(level,count):
    xp=0
    level=int(level)
    count=int(count)
    if level == 1:
        xp=50
    if level == 2:
        xp=100
    if level == 3:
        xp=150
    if level == 4:
        xp=250
    if level ==5:
        xp=500
    if level ==6:
        xp=600
    if level ==7:
        xp=750
    if level ==8:
        xp=900
    if level ==9:
        xp=1100
    if level ==10:
        xp=1200
    if level == 11:
        xp=1600
    if level == 12:
        xp=2000
    if level ==13:
        xp=2200
    if level ==14:
        xp=2500
    if level == 15:
        xp=2800
    if level == 16:
        xp=3200
    if level ==17:
        xp=3900
    if level == 18:
        xp=4200
    if level == 19:
        xp= 4900
    if level == 20:
        xp=5700
    xpThreshold = (xp*count)
    return xpThreshold

def xpHard(level,count):
    xp=0
    level=int(level)
    count=int(count)
    if level == 1:
        xp=75
    if level == 2:
        xp=150
    if level == 3:
        xp=225
    if level == 4:
        xp=375
    if level ==5:
        xp=750
    if level ==6:
        xp=900
    if level ==7:
        xp=1100
    if level ==8:
        xp=1400
    if level ==9:
        xp=1600
    if level ==10:
        xp=1900
    if level == 11:
        xp=2400
    if level == 12:
        xp=3000
    if level ==13:
        xp=3400
    if level ==14:
        xp=3800
    if level == 15:
        xp=4300
    if level == 16:
        xp=4800
    if level ==17:
        xp=5900
    if level == 18:
        xp=6300
    if level == 19:
        xp= 7300
    if level == 20:
        xp=8500

    xpThreshold = (xp*count)
    return xpThreshold

def xpDeadly(level,count):
    xp=0
    level=int(level)
    count=int(count)
    if level == 1:
        xp=100
    if level == 2:
        xp=200
    if level == 3:
        xp=400
    if level == 4:
        xp=500
    if level ==5:
        xp=1100
    if level ==6:
        xp=1400
    if level ==7:
        xp=1700
    if level ==8:
        xp=2100
    if level ==9:
        xp=2400
    if level ==10:
        xp=2800
    if level == 11:
        xp=3600
    if level == 12:
        xp=4500
    if level ==13:
        xp=5100
    if level ==14:
        xp=5700
    if level == 15:
        xp=6400
    if level == 16:
        xp=7200
    if level ==17:
        xp=8800
    if level == 18:
        xp=9500
    if level == 19:
        xp= 10900
    if level == 20:
        xp=12700
    

    xpThreshold = (xp*count)
    return xpThreshold



print('How many characters are in your party?')
playerCount = input()

print('What level are your character?')
playerLevel = input()

playerDifficulty=difficultySet()

if playerDifficulty == 1:
    xpThreshold=xpEasy(playerLevel,playerCount)
if playerDifficulty == 2:
    xpThreshold=xpMedium(playerLevel,playerCount)
if playerDifficulty == 3:
    xpThreshold=xpHard(playerLevel,playerCount)
if playerDifficulty == 4:
    xpThreshold=xpDeadly(playerLevel,playerCount)


#xpThreshold = xpSet(playerLevel,playerCount)

#print(f'You are a {playerCount} player band of level {playerLevel} characters')
print(xpThreshold)
