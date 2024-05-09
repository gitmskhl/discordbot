import discord
from discord.ext import commands
from smartbot.bot import handle as hd 

import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, './smartbot/')

config = {
    'token': [77, 84, 73, 122, 78, 106, 65, 53, 79, 68, 107, 52, 78, 84, 77, 51, 79, 84, 73, 122, 78, 122, 107, 120, 79, 81, 46, 71, 65, 81, 66, 102, 116, 46, 73, 120, 56, 68, 111, 86, 100, 101, 84, 95, 76, 102, 80, 120, 112, 72, 80, 55, 111, 98, 85, 104, 70, 54, 116, 103, 45, 105, 85, 77, 52, 114, 114, 69, 89, 90, 52, 119],
    'prefix': 'prefix',
}

config['token'] = ''.join([chr(x) for x in config['token']])

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
