from disnake.ext import commands
import random
import disnake
class funnies(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name = "найтмер", description = "покажет где есть найтмер")
    async def nightmer(self, inter: disnake.CommandInteraction):
        await inter.response.send_message("нет найтмера плэд")

    @commands.slash_command(name = "комар", description = "спавнит комара")
    async def comar(self, inter: disnake.CommandInteraction):
        await inter.response.send_message(" :mosquito: ")
    @commands.slash_command(name = "угадайка", description="угадай загаданное число от 1 до 100")
    async def guess(self, inter: disnake.CommandInteraction):
        """if int(player_guess) > bot_num:
            player_guess = int(await inter.user.send("Ваше число больше чем загаданное/n Попробуй еще раз: "))
        elif int(player_guess) < bot_num:
            player_guess = int(await inter.user.send("Ваше число меньше чем загаданное/n Попробуй еще раз: "))
        elif int(player_guess) == bot_num:
            await inter.response.send_message("Угадал")"""
        # bot_num = random.randint(1, 100)
        await inter.response.send_message("эта хрень все еще не работает - (\_　\_)。゜zｚＺ")
        # player_guess = await
def setup(bot):
    bot.add_cog(funnies(bot))
