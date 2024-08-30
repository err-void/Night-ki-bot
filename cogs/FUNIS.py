from disnake.ext import commands
import random
import disnake
class FUNIS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name = "найтмер", description = "покажет где есть найтмер")
    async def nightmer(self, inter: disnake.CommandInteraction):
        await inter.response.send_message("нет найтмера плэд")

    @commands.slash_command(name = "комар", description = "спавнит комара")
    async def comar(self, inter: disnake.CommandInteraction):
        await inter.response.send_message(" :mosquito: ")

    @commands.slash_command(name = "8balls", description="Шар дает рандомные ответы ъ")
    async def guess(self, inter: disnake.CommandInteraction):
        response_list = ["Логично.", "Да.", "Нет.", "Вероятно.", "Мне что-то слабо верится.", "Может быть.",
                         "Маловерятно.", "Мне сказали \"да\".", "Мне сказали \"нет\".", "Повтори-ка...",
                         "Я лучше промолчу.", "Сконцетрируйтесь и спросите еще раз.", "Не рассчитывайте на это.",
                         "Это точно.", "Ничего подобного.", "Я не знаю.", "Конечно.", "Хз.", "Но это не точно",
                         'Откуда я знаю?',"на вас упадет собака"]
        await inter.response.send_message(response_list[random.randint(0, len(response_list) - 1)])

    @commands.slash_command(name = "рандом-имя", description="Дает вам рандомное имя, сгенерированного из преффиксов и суффиксов")
    async def rand_name(self, inter: disnake.CommandInteraction):
        pref_list = ["slim","far","river","silly","fat","thin","fish","bat","dark","oak","sly","bush","zen","bark",
                     "cry","slack","soup","grim","hook","dirt","mud","sad","hard","crook","sneak","stink","weird",
                     "fire","soot","soft","rough","cling","scar","niko"]
        suffix_list = ["fox","tail","jaw","whisper","twig","root","finder","nose","brow","blade","fry","seek","wart",
                       "tooth","foot","leaf","stone","fall","face","tongue","voice","lip","ear","hair","bred","shirt","fist","oneshot"]
        pref_list_ru =["стройный", "далекий", "река", "глупый", "толстый", "худой", "рыба", "летучая мышь", "темный", "дуб", "хитрый", "куст"," дзен", "кора",
                     "плачущий", "расслабленный", "суп", "мрачный", "крючок", "грязный", "грязный", "грустный",
                       "жесткий", "мошенник", "красться", "вонючий", "странный","огонь", "сажа", "мягкий", "грубый",
                       "цепляющийся", "шрам","нико"]
        suffix_list_ru =["лиса", "хвост", "челюсть", "шепот", "ветка", "корень", "искатель", "нос", "бровь",
                         "лезвие", "жарить", "искать", "бородавка", "зуб", "нога", "лист", "камень", "падение", "лицо", "язык","голос", "губа", "ухо", "волосы", "породистый", "рубашка", "кулак","ваншот"]
        pref_num = random.randint(0, len(pref_list) - 1)
        suffix_num = random.randint(0, len(suffix_list) - 1)
        pref_chouse_ru = pref_list_ru[pref_num]
        suffix_chouse_ru = suffix_list_ru[suffix_num]
        await inter.response.send_message(f"Ваше рандомное имя - {pref_list[pref_num]} {suffix_list[ suffix_num]}, что переводиться как - {pref_chouse_ru} {suffix_chouse_ru}")


    # @commands.slash_command(name = "угадайка", description="угадай загаданное число от 1 до 100")
    # async def guess(self, inter: disnake.CommandInteraction):
    #     """if int(player_guess) > bot_num:
    #         player_guess = int(await inter.user.send("Ваше число больше чем загаданное/n Попробуй еще раз: "))
    #     elif int(player_guess) < bot_num:
    #         player_guess = int(await inter.user.send("Ваше число меньше чем загаданное/n Попробуй еще раз: "))
    #     elif int(player_guess) == bot_num:
    #         await inter.response.send_message("Угадал")"""
    #     # bot_num = random.randint(1, 100)
    #     await inter.response.send_message("эта хрень все еще не работает - (\_　\_)。゜zｚＺ")
        # player_guess = await
def setup(bot):
    bot.add_cog(FUNIS(bot))
