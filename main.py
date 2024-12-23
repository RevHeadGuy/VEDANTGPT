# app id : 
# public key : 
import discord
import os
import openai

chat = ""

openai.api_key = os.getenv("OPENAI_API_KEY")
token = os.getenv("Sec_Key")


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        global chat 
        chat+= f"{message.author}: {message.content}"
        print(f'Message from {message.author}: {message.content}')
        if self.user!= message.author:
             if self.user in message.mentions:
                 print(chat)
               response = openai.completions.create(
               model="gpt-4o-mini",
               prompt = f""
               temperature=1,
               max_tokens=256,
               top_p=1,
               frequency_penalty=0,
               presence_penalty=0
              )
               channel = message.channel
               messageToSend = response.choices[0].text
               await channel.send(messageToSend)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
