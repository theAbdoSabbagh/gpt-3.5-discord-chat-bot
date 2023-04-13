import discord
import openai
import json
import traceback
from time import strftime
from discord import Message
from discord.ext import commands
from rich import print

CREDENTIALS_FILE = 'credentials.json'

class ChatApp:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.messages = [{"role": "system", "content": "You are a friendly chatbot talking to people inside a Discord server."}]

    def chat(self, message):
        self.messages.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            max_tokens=1024,
            n=1,
            messages=self.messages,
            temperature=0.5,            
        )
        self.messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
        return response["choices"][0]["message"]["content"]

with open(CREDENTIALS_FILE) as f:
    credentials = json.load(f)

bot = commands.Bot(
    command_prefix='!',
    intents=discord.Intents.all(),
    owner_ids=credentials['owner_ids']
)

@bot.listen('on_ready')
async def ready():
    print(f"[bold black][{strftime('%H:%M:%S')}] [bold cyan]Logged into:[bold black] {bot.user} [bold black]| [bold cyan]ID: [bold black]{bot.user.id}")

@bot.listen('on_message')
async def artificial_intelligence(message: Message):
    if message.author.id not in bot.owner_ids:
        return
    
    async with message.channel.typing():
        try:
            response = await bot.loop.run_in_executor(None, bot.chatai.chat, message.content)
            await message.channel.send(response, reference=message)
        except Exception as e:
            exc = traceback.format_exc()
            await message.channel.send(f"An error occurred: ```py\n{exc[:1900]}\n```", reference=message)
            if len(exc) > 2000:
                print(exc)

bot.chatai = ChatApp(credentials['openai_api_key'])
bot.run(credentials['discord_bot_token'])
