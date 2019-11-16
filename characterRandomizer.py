#character randomizer

import random

statList=[]
raceId=[]
playerClass=''
statName=['Strength','Dexterity','Constitution','Wisdom','Intelligence','Charisma']
halfElfList=['Strength','Dexterity','Constitution','Wisdom','Intelligence']
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'z']
race=0

def statRoll (statRoll):
    rolls=[]
    die=0
    while  die < 4:
            statRoll = random.randint(1,6)
            #print (statRoll)
            die+=1
            rolls.append(statRoll)
    rolls.remove(min(rolls)) 
    statTotal = sum(rolls)
    statList.append(statTotal)
    return (statTotal)

def raceSelect(race):
    #race=5
    race= random.randint(1,13)
    if race == 1:
        raceId= ['Dragonborn',1]
    if race == 2:
        raceId= ['Hill Dwarf',2]
    if race == 3:
        raceId= ['High Elf',3]
    if race == 4:
        raceId= ['Forest Gnome',4]
    if race == 5:
        raceId= ['Half-Elf',5]
    if race == 6:
        raceId= ['Lightfoot Halfling',6]
    if race == 7:
        raceId= ['Half-Orc',7]
    if race == 8:
        raceId= ['Human',8]
    if race == 9:
        raceId= ['Tiefling',9]
    if race == 10:
        raceId= ['Wood Elf',10]
    if race == 11:
        raceId= ['Mountain Dwarf',11]
    if race == 12:
        raceId= ['Rock Gnome',12]
    if race == 13:
        raceId = ['Stout Halfling',13]
    
    return(raceId)

def raceMod (raceId):
    if raceId[1]==1:
        statDictionary['Strength']= (statDictionary['Strength']+2)
        statDictionary['Charisma']= (statDictionary['Charisma']+1)
    if raceId[1]==2:
        statDictionary['Constitution']=(statDictionary['Constitution']+2)
        statDictionary['Wisdom']=(statDictionary['Wisdom']+1)
    if raceId[1]==3:
        statDictionary['Dexterity']=(statDictionary['Dexterity']+2)
        statDictionary['Intelligence']=(statDictionary['Intelligence']+1)
    if raceId[1]==4:
        statDictionary['Intelligence']=(statDictionary['Intelligence']+2)
        statDictionary['Dexterity']=(statDictionary['Dexterity']+1)
    if raceId[1]==5:
        statDictionary['Charisma']= (statDictionary['Charisma']+2)
        randomStat=random.choice(list(halfElfList))
        statDictionary[randomStat]= (statDictionary[randomStat]+1)
        randomStat=random.choice(list(halfElfList))
        statDictionary[randomStat]= (statDictionary[randomStat]+1)
    if raceId[1]==6:
        statDictionary['Dexterity']=(statDictionary['Dexterity']+2)
        statDictionary['Charisma']= (statDictionary['Charisma']+1)
    if raceId[1]==7:
        statDictionary['Strength']= (statDictionary['Strength']+2)
        statDictionary['Constitution']= (statDictionary['Constitution']+1)
    if raceId[1]==8:
        statDictionary['Strength']= (statDictionary['Strength']+1)
        statDictionary['Constitution']= (statDictionary['Constitution']+1)
        statDictionary['Dexterity']=(statDictionary['Dexterity']+1)
        statDictionary['Wisdom']=(statDictionary['Wisdom']+1)
        statDictionary['Intelligence']=(statDictionary['Intelligence']+1)
        statDictionary['Charisma']= (statDictionary['Charisma']+1)
    if raceId[1]==9:
        statDictionary['Intelligence']=(statDictionary['Intelligence']+1)
        statDictionary['Charisma']= (statDictionary['Charisma']+2)
    if raceId[1]==10:
        statDictionary['Dexterity']=(statDictionary['Dexterity']+2)
        statDictionary['Wisdom']=(statDictionary['Wisdom']+1)
    if raceId[1]==11:
        statDictionary['Strength']= (statDictionary['Strength']+2)
        statDictionary['Constitution']=(statDictionary['Constitution']+2)
    if raceId[1]==12:
        statDictionary['Intelligence']=(statDictionary['Intelligence']+2)
        statDictionary['Constitution']= (statDictionary['Constitution']+1)
    if raceId[1]==13:
        statDictionary['Dexterity']=(statDictionary['Dexterity']+2)
        statDictionary['Constitution']= (statDictionary['Constitution']+1)
        
def classPick():
    if highStat== 'Strength':
        classSTR = random.randint(1,3)
        if classSTR == 1:
            playerClass= 'Barbarian'
        if classSTR == 2:
            playerClass= 'Fighter'
        if classSTR==3:
            playerClass= ' Paladin'
        return (playerClass)
    if highStat=='Dexterity':
        classDEX= random.randint(1,4)
        if classDEX==1:
            playerClass='Fighter'
        if classDEX==2:
            playerClass='Rogue'
        if classDEX==3:
            playerClass='Ranger'
        if classDEX==4:
            playerClass='Monk'
        return (playerClass)
    if highStat=='Wisdom':
        classWIS=random.randint(1,2)
        if classWIS==1:
            playerClass='Druid'
        if classWIS==2:
            playerClass='Cleric'
        return (playerClass)
    if highStat=='Intelligence':
        playerClass='Wizard'
        return (playerClass)
    if highStat=='Charisma':
        classCHA=random.randint(1,3)
        if classCHA==1:
            playerClass='Bard'
        if classCHA==2:
            playerClass='Sorcerer'
        if classCHA==3:
            playerClass='Warlock'
        return(playerClass)
    if highStat=='Constitution':
        if statDictionary['Strength']>=14:
            classSTR = random.randint(1,3)
            if classSTR == 1:
                playerClass= 'Barbarian'
            if classSTR == 2:
                playerClass= 'Fighter'
            if classSTR==3:
                playerClass= ' Paladin'
            return (playerClass)
        if statDictionary['Dexterity']>=14:
            classDEX= random.randint(1,4)
            if classDEX==1:
                playerClass='Fighter'
            if classDEX==2:
                playerClass='Rogue'
            if classDEX==3:
                playerClass='Ranger'
            if classDEX==4:
                playerClass='Monk'
            return (playerClass)
        if statDictionary['Wisdom']>=14:
            classWIS=random.randint(1,2)
            if classWIS==1:
                playerClass='Druid'
            if classWIS==2:
                playerClass='Cleric'
            return (playerClass)
        if statDictionary['Charisma']>=14:
            classCHA=random.randint(1,3)
            if classCHA==1:
                playerClass='Bard'
            if classCHA==2:
                playerClass='Sorcerer'
            if classCHA==3:
                playerClass='Warlock'
            return(playerClass)
        else:
            playerClass='Wizard'
            return (playerClass)

def characterName(length):
    if length <= 0:
        return False

    full_syl = ''
    for i in range(length):
        decision = random.choice(('consonant', 'vowel'))

        if full_syl[-1:].lower() in vowels:
            decision = 'consonant'
        if full_syl[-1:].lower() in consonants:
            decision = 'vowel'

        if decision == 'consonant':
            syl_choice = random.choice(consonants)
        else:
            syl_choice = random.choice(vowels)

        if full_syl == '':
            full_syl += syl_choice.upper()
        else:
            full_syl += syl_choice

    return full_syl
    
raceId=raceSelect(race)

count=0
while count <6:
    abilityStat = statRoll(0)
    count=count+1

zipStat=zip(statName,statList)
statDictionary=dict(zipStat)
raceMod(raceId)
highStat = (max(statDictionary, key=statDictionary.get))
playerClass = classPick()

for i in range(1):
    length = random.randint(3, 7)
    name =(characterName(length))
#print (raceId[0])
#print(playerClass)
#print(statDictionary)
#print (highStat)
#print(statList)


print (' You are ' + (name) + ' the ' + (raceId[0]) + ' ' + (playerClass))
print ( ' Your ability scores are:')
print (statDictionary)

















