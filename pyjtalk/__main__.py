import sys
from .jtalker import JTalker

context = sys.argv[1]
JTalker().talk(context, outwav="dist/pyjtalk.wav")
