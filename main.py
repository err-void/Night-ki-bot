"""бляздец"""
import os
# import sys
import dotenv
# import asyncio

import disnake
from disnake.ext import commands

dotenv.load_dotenv("conf.env") #IT WORKS
tocken = os.environ.get("tocken")
bot = commands.Bot( command_prefix=['prefix'], intents=disnake.Intents.all(),status = disnake.Status.idle, activity = disnake.Activity(type = disnake.ActivityType.watching, name = "инфернальные крики разрабов"))

# екстеншены
bot.load_extensions(os.path.join('cogs'))

@bot.slash_command(name="ping", description="верент время пинга")
async def ping(inter):
    await inter.response.send_message(f"Ping time {round(bot.latency * 1000)}ms")
@bot.slash_command(description='Загрузить модуль бота')
@commands.is_owner()
async def load(inter: disnake.CommandInteraction, module: str = commands.Param(name="module", description="Название модуля")):
    bot.load_extension(f"cogs.{module}")
    await inter.response.send_message(f"Загружен модуль `{module}`",ephemeral=True)

@bot.slash_command(description='Выгрузить модуль бота')
@commands.is_owner()
async def unload(inter: disnake.CommandInteraction, module: str = commands.Param(name="module", description="Название модуля")):
    bot.unload_extension(f"cogs.{module}")
    await inter.response.send_message(f"Выгружен модуль `{module}`",ephemeral=True)
@bot.slash_command(description="Перезагрузить модуль бота")
@commands.is_owner()
async def reload(inter: disnake.CommandInteraction, module: str = commands.Param(name="module", description="Название модуля")):
    bot.reload_extension(f"cogs.{module}")
    await inter.response.send_message(f"Перезагружен модуль `{module}`",ephemeral=True)

@bot.event
async def on_ready():
    """а что тут писать, тут бот запускаеться"""
    print(f"Logged in as {bot.user} (ID: {bot.user.id})\nREAD FILE PYTHON БЛЯТЬ \n ОКЕЙ БЛЯТЬ\nБИМ БИМ БИМ БИМ БАМ БАМ БАМ БУМ БУМ БУМ БУМ \n СУКА")
bot.run(tocken)
