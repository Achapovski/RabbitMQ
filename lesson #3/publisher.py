import asyncio
import json

import aiormq


async def aiormq_publish():
    connection = await aiormq.connect("amqp://guest:guest@localhost/")
    channel = await connection.channel()

    await channel.exchange_declare(
        exchange="Exchanger",
        exchange_type="direct",
    )

    data = {"message": "Hello world", "message_number": 1}
    while True:
        await asyncio.sleep(2)
        await channel.basic_publish(
            exchange="Exchanger", body=json.dumps(data).encode()
        )
        data["message_number"] += 1

asyncio.run(aiormq_publish())
