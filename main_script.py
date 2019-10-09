from discord.ext import commands
import time
import discord

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("SpamBot is now running")
    await client.change_presence(activity=discord.Game("Use '.spam ?' for info"))
    spam_running = False

@client.command(pass_context=True)
async def spam(ctx, mode = "11381138", *, rep = "a"):
    print("ok")
    if str.lower(mode) == "on":
        await ctx.send(ctx.message.author.mention + "  |  SpamBot has been enabled")
        global spam_running
        spam_running = True
        while spam_running:
            await ctx.send(rep)
            time.sleep(0.5)
    elif str.lower(mode) == "off":
        spam_running = False
        await ctx.send(ctx.message.author.mention + "  |  SpamBot has been disabled")
    elif str.lower(mode) == "11381138" or str.lower(mode) == "?" or str.lower(mode) == "help":
        await ctx.send(ctx.message.author.mention + "  |  This bot will send a message of your choice every half second when enabled\n \n**.spam on *message***  -  Enables spam bot with inputted message\n \n**.spam off**  -  Disables spam bot\n \n**.spam help**  -  Bot info")
    else:
        await ctx.send(ctx.message.author.mention + "  |  That is not the correct use of this command\n \nUse **.spam** for help")



client.run("NjMxMzE3MjkyMTkzNDE1MTY5.XZ1GHw.3msf91qliwYHllrapma-evDso8A")