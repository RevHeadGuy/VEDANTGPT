# app id : *************
# public key : ********************
import discord 
import os
import openai

# file = input("Enter 1, 2, or 3 for loading the chat:\n ")
file = f"chat{file}.txt"
match(file):
  case "1":
    file = "chat1.txt"
  case "2":
    file = "chat2.txt"
  case "3": 
    file = "chat3.txt"
  case _:
    print("Invalid choice.")
    exit()

with open(file, "r") as f:
  chat = f.read() 

openai.api_key = os.getenv("OPENAI_API_KEY")
token = os.getenv("Sec_Key")

user_chats = {}

class MyClient(discord.Client):
    async def on_message(self, message):
        if self.user == message.author:
            return

        if message.author.id not in user_chats:
            user_chats[message.author.id] = ""

        user_chats[message.author.id] += f"{message.author}: {message.content}\n"

        if self.user in message.mentions:
            try:
                response = openai.Completion.create(
                    model="gpt-4",
                    prompt=f"{user_chats[message.author.id]}\nVedantGPT: ",
                    temperature=1,
                    max_tokens=256,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                await message.channel.send(response.choices[0].text.strip())
            except Exception as e:
                print(f"Error: {e}")
                user_chats[message.author.id] = ""


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
