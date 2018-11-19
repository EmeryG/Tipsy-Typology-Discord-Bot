import discord
import asyncio
import sqlite3

adminid = "138400441967837184"
db = sqlite3.connect('data.db')
cur = db.cursor()
print('Connection to database successful!\n-----')
client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
	    addPoints(message.author.name, "1")
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

@client.event
async def on_member_update(before, after):
    if before.name != after.name:
        await updateName(before.name, after.name)

@client.event
async def on_member_join(member):
    try:
        cur.execute("SELECT id FROM players WHERE id = " + member.id)
    except:
        cur.execute("INSERT INTO players ")
    finally:
        db.commit();

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

def updateName(before, after):
    try:
        cur.execute("UPDATE players SET name = " + after.name + " WHERE name = '" + before.name +"'")
    except sqlite3.OperationalError:
        cur.execute("INSERT INTO players VALUES ('" + after.name + "',0,0,'none')")
    finally:
        db.commit()

def addPoints(name, number):
	try:
		cur.execute("SELECT points FROM players WHERE name = '" + name +"'")
		print(str(cur.fetchone()[0]) + "doot")
	except sqlite3.OperationalError:
		cur.execute("INSERT INTO players VALUES ('" + name + "'," + number + "," + number + ",'nada')")
	finally:
		db.commit()

def setTeam(name, team):
	try:
		cur.execute("UPDATE players SET team = " + team + " WHERE name = '" + name +"'")
	except:
		cur.execute("INSERT INTO players VALUES ('" + name + "',0,0,'" + team + "')")
	finally:
		db.commit()

client.run('NTA2NTk4MjY0NjY2MDYyODY4.Drk4cw.7Gy8m9e_T5ncDY370aitXq085OE')

