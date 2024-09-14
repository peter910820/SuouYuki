from discord.ext import commands

class ErrorHandler(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error) -> None:
        await ctx.send(error)
        
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ErrorHandler(bot))