from discord import embeds
import discord
from discord.ext import commands
from discord_slash import SlashContext, cog_ext
from aioconsole import aexec

def setup(bot):
    bot.add_cog(Eval(bot))

class Eval(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="eval", description="Eval code")
    async def eval(self, ctx: SlashContext, *, type, code: str):
        if type == "py":
            result = await aexec(code)
            embed=discord.Embed(title=":white_check_mark: **Python Eval Results**", description=f"**Code**:\n```py\n{code}\n```\n**Result**:\n```sh\n{result}\n```")
            await ctx.send(embed=embed)