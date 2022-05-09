import os
import logging

logger = logging.getLogger(__name__)


PYJTALK_DEFAULT_VOICE_PATH = os.getenv("PYJTALK_DEFAULT_VOICE_PATH") \
    or "/usr/share/pyjtalk/voice/mei/mei_normal.htsvoice"

PYJTALK_DEFAULT_DICTIONARY_PATH = os.getenv("PYJTALK_DEFAULT_DICTIONARY_PATH") \
    or "/var/lib/mecab/dic/open-jtalk/naist-jdic/"


logger.info("config loaded")
