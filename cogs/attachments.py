import discord
from discord.ext import commands

class attachments(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, message):
        channel = self.bot.get_channel(690584660123582494)
        if not message.channel.category_id:
            return
        if not message.channel.category_id == 553232325832343574:
            return

        if message.attachments:
            for i in message.attachments:
                if message.content is not None:
                    embed = discord.Embed(title="shitty shit", description=message.content)
                    embed.set_image(url=i.url)
                    await channel.send(embed=embed)
                else:
                    embed = discord.Embed(title="shitty shit")
                    embed.set_image(url=i.url)
                    await channel.send(embed=embed)
        else:
            return

def setup(bot):
    bot.add_cog(attachments(bot))
