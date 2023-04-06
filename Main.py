import discord
from discord.ext import commands


BOT_TOKEN = "MTA5MzQyNjg5MjEyNTc2NTY5Mw.GyMHNe.syjkwR6Gq26VPDBCU15S4M-cZNcvIXuvB_bigU"
import interactions

bot = interactions.Client(
    token=BOT_TOKEN,
)

@bot.command()
async def info(ctx: interactions.CommandContext):
    """information about the server"""
    await ctx.send("Gamestorm Beta \n Date created: Dec 21, 2022 \n By Shivesh") 
    

bot.start()
