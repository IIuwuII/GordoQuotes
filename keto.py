import discord
from discord.ext import commands
import random
import config
import quotes
import asyncio
from discord.ext.commands import cooldown
 
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
    await bot.change_presence(activity=discord.Game(name=";help | Keylogging Keto"))
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
 
try:
    async def self_check(ctx):
        if 637090083144728576 == ctx.message.author.id:
            return True
        else:
            await ctx.send(f"<@{ctx.author.id}> is not in the sudoers file. This incident will be reported.")
    # A secondary check to ensure nobody but the owner can run these commands.
    # @commands.check(self_check)
 
    @bot.command()
    async def help(ctx):
        embed=discord.Embed(title="Gordo Quotes", url="https://toilet.cat/", description="Quoting bitches since 2019.")
        embed.set_thumbnail(url="https://raw.githubusercontent.com/xstecky/Keto-Bot/master/ketoflake.png")
        embed.add_field(name="Send one of Keto's finest quotes.", value=";ketoquote", inline=False)
        embed.add_field(name="Send one of Human's finest quotes.", value=";humanquote", inline=False)
        embed.add_field(name="Send one of Gay Nasa's finest quotes.", value=";gaynasaquote", inline=False)
        embed.add_field(name="Send one of Gordo's finest quotes.", value=";gordoquote", inline=False)
        embed.add_field(name="Ask the magic 8-Ball a question.", value=";m8b [question]", inline=False)
        embed.add_field(name="Scan for Gordo alts.", value=";gordoalt", inline=False)
        embed.add_field(name="Links the Keto Bot repository.", value=";github", inline=False)
        embed.add_field(name="Make Keto say something. (Owner only)", value=";say [text]", inline=False)
        embed.add_field(name="Change the game status. (Owner only)", value=";changegame [text]", inline=False)
        embed.set_footer(text="© Toilet Cat Technologies") 
        await ctx.send(embed=embed)
        print (f"{ctx.message.author.name} requested the help embed in {ctx.guild.name}!")
    # Help Embed

    @bot.command(pass_context=True)
    async def m8b(ctx):
        messages = ["Yes.", "No.", "Ask Gordo.", "Absolutely.", "Fuck no."]
        await ctx.send(random.choice(messages))
        print (f"{ctx.message.author.name} used the magic 8-Ball in {ctx.guild.name}! ({ctx.message.content})")
    # 8-Ball

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def say(ctx, *, text):
        await ctx.send(text)
        print (f"{ctx.message.author.name} used the say command in {ctx.guild.name}! ({ctx.message.content})")
    # Say

    @bot.command(pass_context=True)
    async def github(ctx):
        await ctx.send('https://github.com/xstecky/Keto-Bot')
        print (f"{ctx.message.author.name} requested the GitHub URL in {ctx.guild.name}!")
    # GitHub

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def changegame(ctx, *, text):
        await bot.change_presence(activity=discord.Game(name=(text)))
        await ctx.send('done :zany_face:')
        print (f"{ctx.message.author.name} changed Keto's status in {ctx.guild.name}! ({ctx.message.content})")
    # Change Game

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def debug(ctx):
        await ctx.send('fuck <@643943061893808148> :rage:')
        print (f"{ctx.message.author.name} debugged in {ctx.guild.name}!")
    # Debug

    @bot.command(pass_context=True)
    async def ketoquote(ctx):
        messages = quotes.keto
        await ctx.send(random.choice(messages))
        print (f"{ctx.message.author.name} requested a Keto quote in {ctx.guild.name}!")
    # Keto Quotes

    @bot.command(pass_context=True)
    async def humanquote(ctx):
        messages = quotes.human
        await ctx.send(random.choice(messages))
        print (f"{ctx.message.author.name} requested a Human quote in {ctx.guild.name}!")
    # Human Quotes

    @bot.command(pass_context=True)
    async def gaynasaquote(ctx):
        messages = quotes.gaynasa
        await ctx.send(random.choice(messages))
        print (f"{ctx.message.author.name} requested a Gay Nasa quote in {ctx.guild.name}!")
    # Gay Nasa Quotes

    @bot.command(pass_context=True)
    async def gordoquote(ctx):
        messages = quotes.gordo
        await ctx.send(random.choice(messages))
        print (f"{ctx.message.author.name} requested a Gordo quote in {ctx.guild.name}!")
    # Gordo Quotes

    @bot.command(pass_context=True)
    @cooldown(1, 16)  # 1000 second cooldown
    async def gordoalt(ctx):
        message = await ctx.send('```SCANNING FOR GORDO ALTS...```')
        await message.edit(content='```SCANNING FOR GORDO ALTS...```')
        await asyncio.sleep(2)
        await message.edit(content='```10%  [▰▱▱▱▱▱▱▱▱▱]```')
        await asyncio.sleep(0.5)
        await message.edit(content='```20%  [▰▰▱▱▱▱▱▱▱▱]```')
        await asyncio.sleep(0.5)
        await message.edit(content='```30%  [▰▰▰▱▱▱▱▱▱▱]```')
        await asyncio.sleep(1)
        await message.edit(content='```40%  [▰▰▰▰▱▱▱▱▱▱]```')
        await asyncio.sleep(2)
        await message.edit(content='```50%  [▰▰▰▰▰▱▱▱▱▱]```')
        await asyncio.sleep(1)
        await message.edit(content='```60%  [▰▰▰▰▰▰▱▱▱▱]```')
        await asyncio.sleep(0.5)
        await message.edit(content='```70%  [▰▰▰▰▰▰▰▱▱▱]```')
        await asyncio.sleep(0.5)
        await message.edit(content='```80%  [▰▰▰▰▰▰▰▰▱▱]```')
        await asyncio.sleep(1)
        await message.edit(content='```90%  [▰▰▰▰▰▰▰▰▰▱]```')
        await asyncio.sleep(2)
        await message.edit(content='```100% [▰▰▰▰▰▰▰▰▰▰]```')
        await asyncio.sleep(2)
        complete = ["```[1] GORDO ALTS DETECTED```", "```758 MEMBERS SCANNED, 1 GORDO ALT FOUND```", "```ATTENTION ALL ADMINS: GORDO ALT IN GENERAL!```"]
        await message.edit(content=random.choice(complete))
    # Scan for Gordo Alts

except:
    pass
import config
bot.run(config.token, bot=True)
