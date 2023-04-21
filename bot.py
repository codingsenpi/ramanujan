import os 
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

    #Listing All Bots Commands
    print('All commands:')
    for command in bot.commands: 
        print(f"{command.name} 🟢")
    
    # Syncing trees
    await bot.tree.sync()
    print('Synced the tree.')

@bot.tree.command()
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message('pong')

bot.run(os.getenv("DISCORD_TOKEN"))
