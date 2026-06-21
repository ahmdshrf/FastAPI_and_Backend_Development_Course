import time
from rich import print

import asyncio

async def endpoint (route:str) -> str:
    print(f">> handling {route}")

    await asyncio.sleep(1)

    print(f"<< response {route}")

    return route

async def server():

    tests = (
        "GET /shipment$id=1",
        "PATCH /shipment$id=4",
        "GET /shipment$id=3",
    )

    start = time.perf_counter()

    for route in tests:
        result = await endpoint(route)
        print("Result back :" , result)

    end = time.perf_counter()

    print(f"Time Taken : {end - start:.2f}s")


asyncio.run(
    server()
)