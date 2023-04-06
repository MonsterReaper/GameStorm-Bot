import os
import discord
from discord.ext import commands
import interactions
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
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
        embed = interactions.Embed(color=interactions.Color.GREEN,title="Information")
        embed.add_field(name="Server",value="GameStorm Beta", inline=False)
        embed.add_field(name="Number of members",value=str(n),inline=False)
        embed.description= "Basic information about the GameStorm server."
        embed.add_field(name="My GitHub", value="https://github.com/monsterreaper")
        embed.set_footer("Created by Shivesh")    
        await ctx.send(embeds=embed)

    except Exception as e:
         print(e)



bot.start()
