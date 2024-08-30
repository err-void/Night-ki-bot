import os
# import sys
import dotenv
# import asyncio

import disnake
from disnake.ext import commands

dotenv.load_dotenv("conf.env") #IT WORKS
tocken = os.environ.get("tocken")
bot = commands.Bot( command_prefix=['prefix'], intents=disnake.Intents.all(),status = disnake.Status.idle,
                    activity = disnake.Activity(type = disnake.ActivityType.listening, name = "хорошую музыку"))

bot.load_extensions(os.path.join('cogs'))

@bot.slash_command(name="ping", description="верент время пинга")
async def ping(inter):
    await inter.response.send_message(f"Ping time {round(bot.latency * 1000)}ms")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})\nREAD FILE PYTHON БЛЯТЬ \n ОКЕЙ БЛЯТЬ\nБИМ БИМ БИМ БИМ БАМ БАМ БАМ БУМ БУМ БУМ БУМ \n СУКА")
bot.run(tocken)
