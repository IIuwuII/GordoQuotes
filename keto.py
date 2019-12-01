import discord
from discord.ext import commands
import random
import config
import quotes
import asyncio
from discord.ext.commands import cooldown
import string
import datetime

start_time = datetime.datetime.utcnow() # Timestamp of when it came online
 
print('  _  __    _        ____        _   ')
print(' | |/ /___| |_ ___ | __ )  ___ | |_ ')
print(' | . // _ \ __/ _ \|  _ \ / _ \| __|')
print(' | . \ __/ ||  (_) | |_) | (_) | |_ ')
print(' |_|\_\___|\__\___/|____/ \___/ \__|')
print(' ')
 
bot = commands.Bot(command_prefix=config.prefix)
bot.remove_command("help")
 
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="On a date with Gordi AI..."))
    print('------')
    print('Ready!')
    print('------')
    print('Logged in as:')
    print(bot.user.name)
    print('------')
    print('Connected to:')
    for server in bot.guilds:
        print(' ')
        print(server.name)
        print(server.id)
    print('------')
    print('© Toilet Cat Technologies')
    print('------')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"<@{ctx.author.id}>, that command doesn't exist. Type ``;help`` to view all my commands.")
 
async def self_check(ctx):
    if 637090083144728576 == ctx.message.author.id:
        return True
    else:
        await ctx.send(f"<@{ctx.author.id}> is not in the sudoers file. This incident will be reported.")
# A secondary check to ensure nobody but the owner can run these commands.

@bot.command()
async def help(ctx):
    now = datetime.datetime.utcnow() # Timestamp of when uptime function is run
    delta = now - start_time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    if days:
        time_format = "{d} days, {h} hours, {m} minutes, and {s} seconds."
    else:
        time_format = "{h} hours, {m} minutes, and {s} seconds."
    uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
    embed=discord.Embed(title="Gordo Quotes", url="https://toilet.cat/", description="Quoting bitches since 2019.")
    embed.set_thumbnail(url="https://raw.githubusercontent.com/xstecky/xstecky.github.io/master/toilet_cat.gif")
    embed.add_field(name="Prefix", value="``;``", inline=False)
    embed.add_field(name="Quotes", value="``ketoquote`` ``humanquote`` ``gaynasaquote`` ``gordoquote`` ``ramsquote``", inline=False)
    embed.add_field(name="Fun", value="``8b`` ``gordoalt``", inline=True)
    embed.add_field(name="Info", value="``github``", inline=True)
    embed.add_field(name="Other", value="``say`` ``changegame``", inline=True)
    embed.set_footer(text="© Toilet Cat Technologies | {}".format(uptime_stamp))
    await ctx.author.send(embed=embed)
    await ctx.send(f"<@{ctx.author.id}>, my commands have been sent to your DMs!")
    print (f"{ctx.message.author.name} requested the help embed in {ctx.guild.name}!")

@bot.command(name='8b')
async def _8b(ctx):
    messages = ["Yes.", "No.", "Ask Gordo.", "Absolutely.", "Fuck no.", "Yes – definitely.", "Bruh. Really?", "Star Keto Bot on GitHub, then I'll answer.", "Error 523: Can't reach toilet.cat/8banswers.json", "Don't count on it.", "I need a Juul hit before I can give an accurate answer."]
    m8b = (ctx.message.content)
    embed=discord.Embed(title="Magic 8-Ball")
    embed.set_thumbnail(url="https://raw.githubusercontent.com/xstecky/Keto-Bot/master/8ballgordo.png")
    embed.add_field(name="Question:", value=(m8b.replace(';8b','')), inline=False)
    embed.add_field(name="Answer:", value=(random.choice(messages)), inline=False)
    embed.set_footer(text="Asked by {}".format(ctx.message.author.name))
    await ctx.send(embed=embed)
    print (f"{ctx.message.author.name} used the magic 8-Ball in {ctx.guild.name}! ({ctx.message.content})")

@commands.check(self_check)
@bot.command()
async def say(ctx, *, text):
    await ctx.send(text)
    print (f"{ctx.message.author.name} used the say command in {ctx.guild.name}! ({ctx.message.content})")

@bot.command()
async def github(ctx):
    await ctx.send('https://github.com/xstecky/Keto-Bot')
    print (f"{ctx.message.author.name} requested the GitHub URL in {ctx.guild.name}!")

@commands.check(self_check)
@bot.command()
async def changegame(ctx, *, text):
    await bot.change_presence(activity=discord.Game(name=(text)))
    await ctx.send('done :zany_face:')
    print (f"{ctx.message.author.name} changed Keto's status in {ctx.guild.name}! ({ctx.message.content})")

@commands.check(self_check)
@bot.command()
async def debug(ctx):
    await ctx.send('fuck <@643943061893808148> :rage:')
    print (f"{ctx.message.author.name} debugged in {ctx.guild.name}!")

@bot.command()
async def ketoquote(ctx):
    messages = quotes.keto
    embed=discord.Embed(title="", description=random.choice(messages))
    embed.set_footer(text="Keto quote requested by {}".format(ctx.message.author.name))
    await ctx.send(embed=embed)
    print (f"{ctx.message.author.name} requested a Keto quote in {ctx.guild.name}!")

@bot.command()
async def humanquote(ctx):
    messages = quotes.human
    embed=discord.Embed(title="", description=random.choice(messages))
    embed.set_footer(text="Human quote requested by {}".format(ctx.message.author.name))
    await ctx.send(embed=embed)
    print (f"{ctx.message.author.name} requested a Human quote in {ctx.guild.name}!")

@bot.command()
async def gaynasaquote(ctx):
    messages = quotes.gaynasa
    embed=discord.Embed(title="", description=random.choice(messages))
    embed.set_footer(text="Gay Nasa quote requested by {}".format(ctx.message.author.name))
    await ctx.send(embed=embed)
    print (f"{ctx.message.author.name} requested a Gay Nasa quote in {ctx.guild.name}!")

@bot.command()
async def gordoquote(ctx):
    messages = quotes.gordo
    embed=discord.Embed(title="", description=random.choice(messages))
    embed.set_footer(text="Gordo quote requested by {}".format(ctx.message.author.name))
    await ctx.send(embed=embed)
    print (f"{ctx.message.author.name} requested a Gordo quote in {ctx.guild.name}!")

@bot.command()
async def ramsquote(ctx):
    messages = quotes.rams
    embed=discord.Embed(title="", description=random.choice(messages))
    embed.set_footer(text="Dieter Rams quote requested by {}".format(ctx.message.author.name))
    await ctx.send(embed=embed)
    print (f"{ctx.message.author.name} requested a Dieter Rams quote in {ctx.guild.name}!")

@bot.command()
@cooldown(1, 16)  # 1000 second cooldown
async def gordoalt(ctx):
    message = await ctx.send('SCANNING FOR GORDO ALTS...')
    await asyncio.sleep(2)
    await message.edit(content='10%  [▰▱▱▱▱▱▱▱▱▱]')
    await asyncio.sleep(0.5)
    await message.edit(content='20%  [▰▰▱▱▱▱▱▱▱▱]')
    await asyncio.sleep(0.5)
    await message.edit(content='30%  [▰▰▰▱▱▱▱▱▱▱]')
    await asyncio.sleep(1)
    await message.edit(content='40%  [▰▰▰▰▱▱▱▱▱▱]')
    await asyncio.sleep(2)
    await message.edit(content='50%  [▰▰▰▰▰▱▱▱▱▱]')
    await asyncio.sleep(1)
    await message.edit(content='60%  [▰▰▰▰▰▰▱▱▱▱]')
    await asyncio.sleep(0.5)
    await message.edit(content='70%  [▰▰▰▰▰▰▰▱▱▱]')
    await asyncio.sleep(0.5)
    await message.edit(content='80%  [▰▰▰▰▰▰▰▰▱▱]')
    await asyncio.sleep(1)
    await message.edit(content='90%  [▰▰▰▰▰▰▰▰▰▱]')
    await asyncio.sleep(2)
    await message.edit(content='100% [▰▰▰▰▰▰▰▰▰▰]')
    await asyncio.sleep(2)
    defaultmembers = 0
    for member in ctx.guild.members:
        if member.avatar == None:
            defaultmembers += 1
    complete = ["ATTENTION ALL ADMINS: GORDO ALT IN GENERAL!"]
    if defaultmembers == 0:
        complete.append(f"{len(ctx.guild.members)} MEMBERS SCANNED, NO GORDO ALTS FOUND")
    elif defaultmembers == 1:
        complete.append(f"{len(ctx.guild.members)} MEMBERS SCANNED, {defaultmembers} GORDO ALT FOUND")
    else:
        complete.append(f"{len(ctx.guild.members)} MEMBERS SCANNED, {defaultmembers} GORDO ALTS FOUND")
    await message.edit(content=random.choice(complete))

import config
bot.run(config.token, bot=True)
