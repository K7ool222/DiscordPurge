from socketxio.socketxio import socketxio

sockets = socketxio()

sockets.send_request('https://google.com', '{"Hello": "World"}')

@Alucard.command()
async def purge(ctx, amount: int): # b'\xfc'
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Alucard.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass