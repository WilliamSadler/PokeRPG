@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await initialise_status()
    await bot_loop()


client.run(TOKEN)