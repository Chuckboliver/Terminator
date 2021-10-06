import discord
import os

from discord import client
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
bot = commands.Bot(command_prefix="$")


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
async def dm(ctx, member: discord.Member, *, content: str):
    await member.send(content)


@bot.event  # Event bot exit from guild
async def on_guild_remove(guild):
    show_server_list()

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None or after.channel is not None:
        if after.channel.id == 702116420753948672:
            ch = discord.utils.get(member.guild.text_channels, name='ดู-ส้มตำ-v2')
            await ch.send("Hey!")

if __name__ == "__main__":
    token = os.getenv("TOKEN")
bot.run(token)
