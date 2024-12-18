import asyncio

from queries.orm import create_table, insert_data


asyncio.run(insert_data())
