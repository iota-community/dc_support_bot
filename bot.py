import re
import discord
import time
import logging
import os
from dotenv import load_dotenv
load_dotenv()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# discord channels filtering
discord_channels = [887252461767786506] #dcverify IF Discord
# discord_channels = [960905086882680833] #test server


class get_main_and_ban(discord.Client):

    # define input to trigger bot
    dc_message_content = ":small_red_triangle: Alt-account intrusion attempt"

    # print to console that we logged in
    async def on_ready(self):
        logger.info('Logged on as', str(self.user))
 
    # the discord function
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

            
        # let's read the message
        if any(x in message.content.casefold() for x in self.dc_message_content) and message.channel.id in discord_channels:
            logger.info("Found the triangle")
            dc_verify_message =  message.content.casefold()

            # print("The original string : " + dc_verify_message)
            try:
                temp = re.findall(r'\d+', dc_verify_message)
                res = list(map(int, temp))

                # print("The numbers list is : " + str(res))

                for i in range(0, len(res)):
                
                    if i == (len(res)-1):
                        continue
                res.reverse()

               # print("The last element of list using reverse : "
               #      + str(res[0]))

                
                await message.channel.send("Bye bye " + str(res[0]))
                userid_to_ban = int(res[0])
                #print("The variable " + str(userid_to_ban))    
                        
                await message.guild.ban(discord.Object(id=userid_to_ban))
                logger.info("and gone")
            except:
                logger.info("not an ALT account message")
    
# load discord intents
intents = discord.Intents.default()
intents.messages = True
intents.bans = True
client = get_main_and_ban(intents=intents)
discord_bot_token = os.getenv("DISCORD_BOT_TOKEN")
client.run(discord_bot_token)
