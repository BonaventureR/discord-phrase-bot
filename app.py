import os
import discord
import random
import asyncio
from dotenv import load_dotenv
from collections import defaultdict

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


class PogClient(discord.Client):
    randomNumberGenerator, message_count, last_author = 1, 0, ""
    rng_lowerbound, rng_upperbound = 750, 1500
    leader_board = spammer_alert = defaultdict(int)
    messages = []

    async def on_ready(self):
        guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n'
        )
        
        print('Starting with RNG', self.randomNumberGenerator)
        
        
    async def on_message(self, message):
        if message.author == client.user:
            return
        
        author = str(message.author).split("#")[0]
        
        self.change_message()
        self.change_spammer_alert(author)
        
        if self.spammer_alert[author] >= 10:
            await message.channel.send("Please stop spamming, you're being cringe. You have " + str(self.spammer_alert[author]) + " consecutive messages.")

        if self.last_author != author:
            self.spammer_alert[self.last_author] = 0
            self.last_author = author
        
        if not (self.message_count % 10):
            print(self.message_count)

        if message.content.lower() == "!leaderboard":
            await message.channel.send("Current Leader Board: \n" + self.stringify_leader_board())
            
#        if message.content.lower() == "!message_count":
#            await message.channel.send("Current Message Count: " + str(self.message_count))
            
        if self.message_count == self.randomNumberGenerator:
            await message.channel.send(random.choice(self.messages))
            if self.randomNumberGenerator != 1:
                self.update_leader_board(author)
            self.reset_message()
            self.changeRNG()
            # recurse
            await self.on_message(message)
    
    def change_spammer_alert(self, author):
        self.spammer_alert[author] += 1
        
    def changeRNG(self):
        print('Reseting RNG ...')
        self.randomNumberGenerator = random.randint(self.rng_lowerbound,self.rng_upperbound)
        
    def change_message(self):
        self.message_count += 1
        
    def reset_message(self):
        print('Reseting Message Count ...')
        self.message_count = 0
        
    def stringify_leader_board(self):
        s = ""
        
        for name, count in reversed(sorted(self.leader_board.items(), key=lambda item: item[1])):
            s += str(name) + " : " + str(count)
            s += "\n"
            
        return str(s)
        
    def update_leader_board(self, author):
        self.leader_board[author] += 1
    

client = PogClient()
client.run(TOKEN)
