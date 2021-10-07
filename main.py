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

@bot.event  # Event bot exit from guild
async def on_guild_remove(guild):
    show_server_list()

@bot.event  # Event bot join guild
async def on_guild_join(guild):
    show_server_list()


@bot.command()
async def dm(ctx, member: dc.Member, *, content: str):
    await member.send(content)

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None or after.channel is not None:
        if after.channel.id == 702116420753948672:
            ch = dc.utils.get(member.guild.text_channels, name='ดู-ส้มตำ-v2')
            await ch.send("Hey!")


@bot.command()
async def clear(ctx, *, content: int):
    deleted = await ctx.message.channel.purge(limit=content)
    await ctx.message.channel.send('Deleted {} message(s)'.format(len(deleted)),delete_after=3)

if __name__ == "__main__":
    load_dotenv()
    token = os.environ.get("TOKEN")
    bot.run(token)
