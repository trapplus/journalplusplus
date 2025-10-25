import asyncio
import logging
import sys

from src import container as cont


async def main() -> None:
    
    await cont.objects.dp.start_polling(cont.objects.bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    asyncio.run(main())
