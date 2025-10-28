import asyncio

async def brew_chai():
    print("brwing chai..")
    await asyncio.sleep(2)
    print("chai is ready")
    
asyncio.run(brew_chai())    