import asyncio
import logging

from pyjtalk.jtalker import JTalker, AsyncJTalker


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

JTalker().synthesize_wav('いぬ', filename='dist/sync-test.wav')


async def main():
    await AsyncJTalker().synthesize_wav(context='猫のテスト', filename='dist/async-test.wav')

logger.debug('before main')
asyncio.run(main())
logger.debug('after main')
