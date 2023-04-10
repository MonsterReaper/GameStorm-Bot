import os
import discord
from discord.ext import commands
import interactions
from dotenv import load_dotenv
import datetime

from Data import msg_count, word_freq_dict
import typing

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = interactions.Client(
    token=BOT_TOKEN
)


@bot.command(
name="info",
description="Provides you the necessary information.",
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
        x = ctx.user.id 
        await ctx.send(embeds=embed)
        await ctx.send(f"<@{x}>")

    except Exception as e:
        print(e)

@bot.command(name="reminder",
    description="Reminds you about something",
    options=[
    {
    "name": "hours",
    "description": "The exact hour when I should remind you",
    "type": 4,
    "required": True
    },
    {
    "name": "minutes",
    "description": "The exact minute of the hour when I should remind you",
    "type": 4,
    "required": True
    },
    {
    "name": "reason",
    "description": "About what should I remind you? ",
    "type": 3,
    "required": True}])

async def reminder(ctx: interactions.CommandContext,hours: int, minutes: int, reason: str):
    await ctx.send(f"I will remind you about {reason} at {hours}:{minutes}")
    
    not_reminded = True
    y = str(hours) + ':' + str(minutes)
    while not_reminded:
        now = datetime.datetime.now()
        et = now.strftime("%H:%M")
        print("Not yet")
        
        if et == y:    
            x = ctx.user.id
            embed = interactions.Embed(color=interactions.Color.GREEN,title="Reminder")
            embed.add_field(name="Reminder was set for",value=f"{hours}:{minutes}", inline=False)
            embed.add_field(name=f"{ctx.user.username}",value=str("!Time is up"),inline=False)
            embed.description= f"Reminding you about {reason}"
            embed.add_field(name="My GitHub", value="https://github.com/monsterreaper")
            embed.set_footer("Created by Shivesh")   
            await ctx.send(f"<@{x}>")
        
            await ctx.send(embeds=embed)
            not_reminded = False
    
    
@bot.command(
name="activity",
description="Shows the activity of the server"
)

async def activity(ctx: interactions.CommandContext):
    embed = interactions.Embed(color=interactions.Color.BLURPLE)
    embed.description="Pie chart of activities"
    x = "https://photos.google.com/photo/AF1QipP7_1bJphrRc8fgYpRs_M1yoiKFTMM3QDwjt-1l"
    embed.set_footer("By Shivesh")
    embed.add_field(name="My GitHub", value="https://github.com/monsterreaper")
    await ctx.send(embeds=embed)
    

@bot.command(
name="my_activity",
description="Shows the activity of the server"
)

async def my_activity(ctx: interactions.CommandContext):
    user = ctx.user.username
    embed = interactions.Embed(title="Your Activities",color=interactions.Color.BLURPLE)
    embed.description="Your activities"
    embed.add_field(name="Message Count", value=f"{msg_count[user]} messages")
    embed.add_field(name="Top 5 words", value=str(word_freq_dict[user]).replace("{","").replace("}","").replace("'",""))
    x = ctx.user.avatar_url
    embed.set_image(x)
    embed.set_footer("By Shivesh")
    embed.add_field(name="My GitHub", value="https://github.com/monsterreaper")
    await ctx.send(embeds=embed)

@bot.command(
    name="avatar",
    description="Shows the user's avatar",
)
async def avatar(ctx: interactions.CommandContext,user: typing.Optional[discord.Member]=None):
    embed = interactions.Embed(title="Avatar",color=interactions.Color.FUCHSIA)
    

    embed.description=f"{ctx.user.username}'s avatar:"
    

    embed.set_image(ctx.user.avatar_url)
    
    embed.set_footer("By Shivesh")
    await ctx.send(embeds=embed)





bot.start() 
