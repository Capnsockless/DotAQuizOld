import random
import discord
import json
import os
from discord.ext import commands

os.chdir(r"D:\Discordbot\DotaQuizbot")

def open_json(jsonfile):
    with open(jsonfile, "r") as fp:      #load the users.json file
        return json.load(fp)       #openfunc for jsonfiles

def save_json(jsonfile, name):           #savefunc for jsonfiles
    with open(jsonfile, "w") as fp:
        json.dump(name, fp)

class Miscellaneous(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def oversight(self, ctx):
        await ctx.send("The biggest oversight with Dark Willow is that she's unbelievably sexy. I can't go on a hour of my day without thinking about plowing that tight wooden ass. I'd kill a man in cold blood just to spend a minute with her crotch grinding against my throbbing manhood as she whispers terribly dirty things to me in her geographically ambiguous accent.")

    @commands.command()
    async def hohoohahaa(self, ctx):
        await ctx.send(file=discord.File('snoper.png'))

    @commands.command()
    async def newpatch(self, ctx):
        rng = open_json("rngfix.json")
        id = str(ctx.guild.id)
        if id not in rng.keys():
            rng[id] = {"questnumbers": "[]", "shopkeepnumbers":"[]", "iconquiznumbers":"[]", "vacuumcd":16}
        rng[id]["vacuumcd"] += random.randint(1, 3)
        await ctx.send(f"""Vacuum cooldown has been increased, it is now **{rng[id]["vacuumcd"]}** seconds long.""")
        save_json("rngfix.json", rng)

    async def cog_command_error(self, ctx, error):
        raise error

def setup(bot):
    bot.add_cog(Miscellaneous(bot))
