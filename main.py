# bot.py
import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

#####################################

@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )

bot = commands.Bot(command_prefix='!sam ')

@bot.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        'Cool. Cool cool cool cool cool cool cool, no doubt no doubt no doubt no doubt.',
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command(name='test')
async def pm(ctx, user: discord.Member = 203081913668206592, *, message="HI I am doing a test"):
    if user is None:
        await ctx.send("No one to send DM to")
    if user is not None:
        await ctx.send("Sending Message")
        if message is None:
            await ctx.send("No Message... huh?")
        if message is not None:

            myembed = discord.Embed()
            myembed.add_field(name=f"(ctx.author) sent you:", value=f"(message")
            myembed.set_footer(text="If this message is...")
            await user.send(embed=myembed)

bot.run(TOKEN)