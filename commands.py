from config import *
from tools import list_commands
from content import *
from interface import twitch_api as twitch


###CUSTOM COMMMANDS BELOW###
del_coms = list()

@bot.command(name='addcom')
async def addcom(ctx):
	#Add 2 limit for some reason to cut into key and val
	ukey,uval = ctx.content.split(" ", 2)[1:]
	if ctx.author.is_mod == True:
		check = comchk(ukey,uval)
		if check:
			await ctx.send("Command added!")

		if not check:
			await ctx.send("This command already exists!")

@bot.command(name='delcom')
async def delcom(ctx):
	#Add 2 limit for some reason to cut into key and val
	ukey = ctx.content.split(" ", 2)[1]
	#TODO: Add function to actually delete command from generator
	check = DelCom(ukey)
	if check:
		await ctx.send("Command deleted!")
		del_coms.append(ukey)

	if not check:
		await ctx.send("This command does not exist.")





#############################



class CommandGenerator:
    'Generates commands based on key-value pairs in dict object in content.py'
    ###Integrate viewers custom commands###

    commands = list()  # listyboi

    def __init__(self, name, response):
        # add the command to the list
        CommandGenerator.commands.append(name)

        # generate the bot.command
        @bot.command(name=name)
        async def call_and_response(ctx):
            await ctx.send(response)


# generate the commands
for cmd, response in faq_info.items():
    CommandGenerator(cmd, response)


# generate the faq help command
@bot.command(name='faq', aliases=['help'])
async def faq(ctx):
    commands = list_commands(CommandGenerator.commands)

    for msg in commands:
        await ctx.send(msg)
