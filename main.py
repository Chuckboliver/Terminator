import discord as dc
import os
from discord.ext import commands
from dotenv import load_dotenv

intents = dc.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="?", intents=intents)


@bot.event
async def on_ready():
    print("Started!!!")


def show_server_list():
    num = 1
    print(f"Bot run on {len(bot.guilds)}")
    for guild in bot.guilds:
        print(f"{num}. Sv: {guild.name} ---> {guild.id}")
        num += 1


@bot.event  # Event bot join guild
async def on_guild_join(guild):
    show_server_list()


@bot.command()
async def dm(ctx, member: dc.Member, *, content: str):
    await member.send(content)


@bot.event  # Event bot exit from guild
async def on_guild_remove(guild):
    show_server_list()

if __name__ == "__main__":
    load_dotenv()
    token = os.environ.get("TOKEN")
    bot.run(token)