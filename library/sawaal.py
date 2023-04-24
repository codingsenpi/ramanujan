import discord
from datetime import datetime

class Sawaal:
    def __init__(self, id, text, image_url, answer, votes, choices, created_at):
        self.id = id 
        self.text = text
        self.image_url = image_url
        self.answer = answer
        self.votes = votes
        self.choices = choices
        self.created_at = created_at

def Sawaal_Embed(sawaal: Sawaal):
    embed = discord.Embed(title="", description=f"**{sawaal.text}**", color=0x00ff00, timestamp=sawaal.created_at)
    embed.set_image(url=sawaal.image_url)
    embed.set_footer(text=f"Id: {sawaal.id} | Votes: {sawaal.votes}")

    return embed

#async def Sawaal_Buttons(sawaal: Sawaal):
    
    #TODO 😇

