import os
import logging

logger = logging.getLogger(__name__)


PYJTALK_DEFAULT_VOICE_PATH = os.getenv("PYJTALK_DEFAULT_VOICE_PATH") \
    or "/etc/pyjtalk/voice/mei/mei_normal.htsvoice"

PYJTALK_DEFAULT_DICTIONARY_PATH = os.getenv("PYJTALK_DEFAULT_DICTIONARY_PATH") \
    or "/etc/pyjtalk/dictionary"


logger.info("config loaded")
