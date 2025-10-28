import asyncio
import time
async def brew(name):
    print(f"Brewing {name}....")
    time.sleep(3)
    print(f"{name} is ready")
    
async def main():
    await asyncio.gather(
        brew("Masala chai"),
        brew("green tea"),
        brew("ginger masala"),
    )    
    
    
asyncio.run(main())    