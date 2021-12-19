import discord as dc
from discord.ext import commands
import random

class GameResultMixin:
    def win():
        pass
    
    def lose():
        pass

    def draw():
        pass

class Roshambo(commands.Cog, GameResultMixin):

    ROCK = 1
    PAPER = 2
    SCISSOR = 3

    __possible_choices = {ROCK, PAPER, SCISSOR}

    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    def win():
        return "Win"

    def lose():
        return "Lose"

    def draw():
        return "Draw"

    def message_parser(self, message: str):
        message = message.lower()
        if message == "rock":
            return self.ROCK
        elif message == "paper":
            return self.PAPER
        elif message == "scissor":
            return self.SCISSOR
        else:
            return None

    def get_choice(self):
        return random.choice(self.possible_choices)

    def get_possible_choice(self):
        return self.__possible_choices

    def evaluate(self, choice, bot_choice):
        if bot_choice == choice:
            return self.draw()
        if choice == self.ROCK:
            if bot_choice == self.SCISSOR:
                return self.win()
            elif bot_choice == self.PAPER:
                return self.lose()
        elif choice == self.PAPER:
            if bot_choice == self.ROCK:
                return self.win()
            elif bot_choice == self.SCISSOR:
                return self.lose()
        elif choice == self.SCISSOR:
            if bot_choice == self.PAPER:
                return self.win()
            elif bot_choice == self.ROCK:
                return self.lose()

    @commands.Cog.listener()
    async def on_message(self, message: str):
        if message.startswith(self.bot.command_prefix):
            choice = self.message_parser(message[1:])
            if choice in self.get_possible_choice():
                bot_choice = self.get_choice()
                respond = self.evaluate(choice, bot_choice)
                await message.channel.send(respond)