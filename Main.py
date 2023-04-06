
BOT_TOKEN = "MTA5MzQyNjg5MjEyNTc2NTY5Mw.GyMHNe.syjkwR6Gq26VPDBCU15S4M-cZNcvIXuvB_bigU"
import discord
from discord.ext import commands
import interactions

bot = interactions.Client(
    token=BOT_TOKEN,
)


@bot.command(
name="info",
description="Provides you the necessary information."
)
async def info(ctx: interactions.CommandContext):
    n = ctx.guild.member_count
    try:
        embed = interactions.Embed(color=interactions.Color.GREEN,title="Information",footer={"Creator":"By Shivesh"})
        embed.add_field(name="Server",value="GameStorm Beta", inline=False)
        embed.add_field(name="Number of members",value=str(n),inline=False)
        embed.description= "Basic information about the GameStorm server."
        embed.add_field(name="GitHub", value="https://github.com/monsterreaper")
    
        await ctx.send(embeds=embed)

    except Exception as e:
         print(e)



bot.start()
