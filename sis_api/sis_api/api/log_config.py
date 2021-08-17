from logging import INFO
from asyncio import sleep
from sys import exc_info
from aiologger.formatters.base import Formatter
from aiologger.handlers.streams import AsyncStreamHandler
from aiologger.handlers.files import AsyncFileHandler


def log_config(logger):
    file_handler = AsyncFileHandler("/code/logs/sis.log")
    stream_handler = AsyncStreamHandler(level=INFO)

    formatter = Formatter("%(asctime)s : %(levelname)s : %(message)s")
    file_handler.formatter = formatter
    stream_handler.formatter = formatter

    logger.add_handler(file_handler)
    logger.add_handler(stream_handler)


async def log_info(logger, message):
    await sleep(0.01)
    logger.info(message)


async def log_error(logger, message):
    await sleep(0.01)
    logger.error(message, exc_info=True)
