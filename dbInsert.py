import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('DnD.db')
c = conn.cursor()

def start():
	while True:
		print('Would you like to enter a new monster in to the database?Y/N')
		start=input()
		if start==('Y'):
			break

def characterInsert():
	while True:
		print('Monster name:')
		monsterName= input()
		if monsterName==('exit'):
			break
		print('XP:')
		monsterXp=input()
		
		c.execute("INSERT INTO monsters (name,xp,challenge)VALUES (?,?,?)" ,
				(monsterName,monsterXp,monsterXp))
		conn.commit()




start()
characterInsert()
conn.close()
