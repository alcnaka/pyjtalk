import os
import logging

from dotenv import load_dotenv

logger = logging.getLogger(__name__)


load_dotenv()

PYJTALK_DEFAULT_VOICE_PATH = os.getenv("PYJTALK_DEFAULT_VOICE_PATH") \
    or "/usr/share/open_jtalk/voices/mei/mei_normal.htsvoice"

PYJTALK_DEFAULT_DICTIONARY_PATH = os.getenv("PYJTALK_DEFAULT_DICTIONARY_PATH") \
    or "/var/lib/mecab/dic/open-jtalk/naist-jdic/"


logger.info("config loaded")
