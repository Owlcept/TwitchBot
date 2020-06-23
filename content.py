import commands

faq_info = {}

with open('command.txt', 'r') as f:
		f1 = f.readlines()
		for x in f1:
			key, val = x.strip('\n').split(" ", maxsplit = 1)
			faq_info[key] = val
			#print('command added successfully!')
		f.close()


#This creates a dictionary with commands and allows custom commands to be created!

def comchk(ukey, uval):
	
	if ukey in commands.CommandGenerator.commands:
		print('Sorry this command already exists!')
		return False
	else:
		AddCom(ukey,uval)
		print('command added successfully!')
		return True

def AddCom(ukey,uval):

	with open('command.txt', 'a+') as f:
		f.write(ukey+' '+uval+'\n')
		f.close()
	faq_info[key] = val
	try:
		commands.CommandGenerator(ukey, uval)
	except:
		pass


def DelCom(ukey):

	if ukey in commands.CommandGenerator.commands:
		commands.CommandGenerator.commands.remove(ukey)
		del faq_info[ukey]
		with open("command.txt", "r+") as f:
		    d = f.readlines()
		    f.seek(0)
		    for i in d:
		        if ukey not in i:
		        	f.write(i)
		    f.truncate()
		    f.close()
		return True

	if ukey not in commands.CommandGenerator.commands:
		return False
