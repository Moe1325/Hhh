import asyncio
from bleak import BleakScanner

async def ble_spammer():
    while True:
        devices = await BleakScanner.discover()
        print("Discovered devices:")
        for device in devices:
            print(device)

        await asyncio.sleep(1)  # Interval between spams

loop = asyncio.get_event_loop()
loop.run_until_complete(ble_spammer())
