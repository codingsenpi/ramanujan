import os, sys
from datetime import datetime
import discord
import discord.ext.commands as commands
from discord import app_commands

sys.path.insert(0, 'library')
from sawaal import Sawaal, Sawaal_Embed, Sawaal_Buttons


sample_sawaal = Sawaal(id=6942069, text="Q. ""Full form of NIGA", image_url="https://static.wikia.nocookie.net/gtawiki/images/2/29/CarlJohnson-GTASAde-Infobox.png", answer="A", votes=173314, choices=["NIGA", "Neutral Isolated Gaseous Atom", "OPTION", "ANOTHER OPTION"], created_at=datetime.now())
sample_sawaal_embed = Sawaal_Embed(sawaal=sample_sawaal)
sample_sawaal_buttons = Sawaal_Buttons(sawaal=sample_sawaal)        

class Academics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command()
    async def sawaal(self, interaction: discord.Interaction):
        await interaction.response.defer()
        await interaction.response.send_message("", embed=sample_sawaal_embed, components=[sample_sawaal_buttons])

async def setup(bot: commands):
    await bot.add_cog(Academics(bot))
