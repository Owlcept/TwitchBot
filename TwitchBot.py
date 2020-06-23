from config import *
from interface import twitch_api as twitch
from clash_module import clash_api as clash 
from commands import *
from ranks import *



@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{BOT_NICK} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    for x in CHANNEL:
        #await ws.send_privmsg(x, f"/me has landed!")

        await set_users(x)




@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == BOT_NICK.lower():

        return

    await bot.handle_commands(ctx)
    print(f"@{ctx.author.name}: {ctx.content}")

    #if ctx.content.split("!", 2)[0] in del_coms:
        #pass
    
    """
    if 'hello' in ctx.content.lower():

        await ctx.channel.send(f"Hi, @{ctx.author.name}!")

    if 'subscriber' in ctx.author.badges and ctx.author not in twitch.greeted_subs and ctx.author != CHANNEL: 
        months_subbed = int(ctx.author.tags['badge-info'].split('/')[1])

        # customize the following lines for custom greetings (based on subs)
        greetings = [
            (24, f" @{ctx.author.name} has arrived! They've been supporting for {months_subbed} flippin months! "),
            (12,f" @{ctx.author.name} is BACK! Thanks for the continued support of {months_subbed} months!"),
            (9, f" @{ctx.author.name} had landed! Congrats on the sub baby and the support of {months_subbed} months!"),
            (6, f" @{ctx.author.name} has arrived! Thanks for the {months_subbed} months support!"),
            (3, f" @{ctx.author.name} is here! Welcome back! {months_subbed} months of support"),
        ]

        for month, message in greetings:
            if months_subbed >= month:
                await ctx.channel.send(message)
                break
        
        twitch.mark_as_greeted(ctx.author)
    """
    with open('users.json', 'r') as f:

        g = json.load(f)
        f.close()
        d = await update_data(g,ctx.author)
        #await update_exp(d)
    with open('users.json', 'w') as f:

        data = json.dumps(d, indent=4)
        f.write(data)
        f.close()


@bot.command(name='modules')
async def test(ctx):
    await ctx.send('Here are currently supported Modules:\n Clash')


@bot.command(name='clear')
async def clear(ctx):
    #check if sender is mod - mod commands
    if ctx.author.is_mod == True:

        await ctx.clear()

@bot.command(name='clash', aliases=['coc'])
async def clash(ctx):
    tag = ctx.content.split(' ')[1]
    print(tag)
    #if clash_mod:

        #clash.SUBMITC(tag)
        #await ctx.send(clan)

    if not clash_mod:
        await ctx.send('The Clash of Clans module is currently off.')

#@bot.command(name='ban')
#async def ban(ctx, name):

if __name__ == "__main__":
    bot.run()