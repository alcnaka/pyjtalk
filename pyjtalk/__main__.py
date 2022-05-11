import sys
from .jtalker import JTalker

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


context = sys.argv[1]
JTalker().synthesize_wav(context, filename="dist/pyjtalk-main.wav")
