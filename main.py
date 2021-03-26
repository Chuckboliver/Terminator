import discord
import os
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix="?")


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


if __name__ == "__main__":
    with open("token.txt", "r") as token_file:
        token = token_file.read()
bot.run(token)
