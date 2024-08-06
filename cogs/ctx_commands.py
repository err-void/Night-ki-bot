import disnake
from disnake.ext import commands
import random

class ctx_commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

#-------------------------Повторялка-------------------------

    @commands.slash_command(name="say", aliases=["s"]) #aliases позволяет добавить команды на которые бот будет так же отзываться
    async def say_command(self, ctx, arg): #arg можно заменить на что угодно, это ваш собственный параметр
        await ctx.send(arg)

#-------------------------Рандомайзер-------------------------

    @commands.slash_command(name="random", aliases=["rand", "r"])
    async def rand_command(self, ctx, min, max):
        randomaizer = random.randint(int(min),int(max))
        await ctx.send(f"Ваше число: {randomaizer}") #f перед кавычками позволяют добавлять аргументы в фигурных {} скобках

def setup(bot):
    bot.add_cog(ctx_commands(bot))