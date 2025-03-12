import discord
from dotenv import load_dotenv
import os
from discord.ext import commands
from discord import app_commands

load_dotenv()

token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

class Comandos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="ping", description="Responde com pong!")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("pong!")

@bot.event
async def on_ready():
    print(f'Bot is ready: {bot.user.name}')
    try:
        await bot.add_cog(Comandos(bot))
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

bot.run(token)