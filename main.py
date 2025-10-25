import asyncio
import logging
import sys

from src import container as cont

disp = cont.objects.dp


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls

    await disp.start_polling(cont.objects.bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
