from config import *
import json

#Open/close redundancies but looks better than leaving file open

async def set_users(x):
	chatters = await bot.get_chatters(x)

	try:
		f = open('users.json')
		f.close()
		return
	except:

		with open('users.json', 'w') as f:

			await set_data(f, chatters)

async def set_data(f, chatters):
	users = {}
	for x in chatters.all:
		users[x] = {
		"experience":0,
		"level":1
		}
		

	data = json.dumps(users, indent=4)
	f.write(data)
	f.close()


async def update_level(d, x):
		d[x]['level'] += 1



async def update_exp(d):
	for x in d:
		d[x]['experience'] += 15
		if d[x]['experience'] == 100 :
			d[x]['experience'] = 0
			await update_level(d,x)

async def update_data(d, x):
	
	if not x in d:
		d[x] = {
		"experience":0,
		"level":1
		}
	return d