from discord.ext import commands, tasks
import time
import discord


client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("SpamBot is now running")
    spam_running = False
    change_status.start()

locked = False
spamcount = 0

if type(spamcount) is int

@client.command(pass_context=True)
async def spam(ctx, mode = "11381138", *, rep = "a"):
    global spamcount
    global locked
    if str.lower(mode) == "lock" and str(ctx.message.author.id) == "402344993391640578":
        await ctx.send(ctx.message.author.mention + "  |  SpamBot has been locked")
        locked = True
    elif str.lower(mode) == "lock" and str(ctx.message.author.id) != "402344993391640578":
        await ctx.send(ctx.message.author.mention + "  |  You do not have permission to use this command")
    elif str.lower(mode) == "unlock" and str(ctx.message.author.id) == "402344993391640578":
        await ctx.send(ctx.message.author.mention + "  |  SpamBot has been unlodked")
        locked = False
    elif str.lower(mode) == "unlock" and str(ctx.message.author.id) != "402344993391640578":
        await ctx.send(ctx.message.author.mention + "  |  You do not have permission to use this command")
    elif str.lower(mode) == "on" and not locked:
        await ctx.send(ctx.message.author.mention + "  |  SpamBot has been enabled")
        global spam_running
        spam_running = True
        while spam_running:
            await ctx.send(rep)
            spamcount += 1
            time.sleep(0.5)
    elif str.lower(mode) == "off" and not locked:
        spam_running = False
        await ctx.send(ctx.message.author.mention + "  |  SpamBot has been disabled")
    elif str.lower(mode) == "11381138" or str.lower(mode) == "?" or str.lower(mode) == "help":
        await ctx.send(ctx.message.author.mention + "  |  This bot will send a message of your choice every half second when enabled\n \n**.spam on *message***  -  Enables spam bot with inputted message\n \n**.spam off**  -  Disables spam bot\n \n**.spam help**  -  Bot info")
    elif locked:
        await ctx.send(ctx.message.author.mention + "  |  SpamBot is currently locked")
    else:
        await ctx.send(ctx.message.author.mention + "  |  That is not the correct use of this command\n \nUse **.spam** for help")

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(str(spamcount // 1000) + " thousand spams!"))

client.run("NjMxMzE3MjkyMTkzNDE1MTY5.XZ1GHw.3msf91qliwYHllrapma-evDso8A")