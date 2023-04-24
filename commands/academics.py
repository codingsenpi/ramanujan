import os, sys
from datetime import datetime
import discord
import discord.ext.commands as commands
from discord import app_commands

sys.path.insert(0, 'library')
from sawaal import Sawaal, Sawaal_Embed
from database_service import get_random_sawaal

class Academics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command()
    async def sawaal(self, interaction: discord.Interaction):
        sawaal = get_random_sawaal()
        sawaal_embed = Sawaal_Embed(sawaal=sawaal)
        await interaction.response.send_message("", embed=sawaal_embed)

async def setup(bot: commands):
    await bot.add_cog(Academics(bot))
