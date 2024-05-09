import discord
from discord.ext import commands
from smartbot.bot import handle as hd 

import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, './smartbot/')

config = {
    'token': 'MTIzNjA5ODk4NTM3OTIzNzkxOQ.GrX9J5.T8ykuBNTttcM5D6nnLQnD-yG2-_7Lyy-w6DX-E',
    'prefix': 'prefix',
}

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

@bot.event
async def on_message(ctx):
	if ctx.author != bot.user:
		query = ctx.content
		print(query)
		reply = hd(query)
		if reply is not None and reply != '':
			await ctx.reply(reply)
	

bot.run(config['token'])
