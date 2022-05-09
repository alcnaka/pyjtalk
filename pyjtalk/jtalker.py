import asyncio
import subprocess
from typing import Optional
import os

from .config import PYJTALK_DEFAULT_DICTIONARY_PATH, PYJTALK_DEFAULT_VOICE_PATH


class BaseJTalker:
    """Base class of JTalker"""

    def __init__(
        self,
        default_dictionary_path: Optional[str] = None,
        default_voice_path: Optional[str] = None,
    ) -> None:
        self.default_dictionary_path = default_dictionary_path or PYJTALK_DEFAULT_DICTIONARY_PATH
        self.default_voice_path = default_voice_path or PYJTALK_DEFAULT_VOICE_PATH

        # TODO: make default params to be configured.
        self.default_openjtalk_command = 'open_jtalk'
        self.default_speed = 1.0
        self.default_picth = 0.0
        self.default_vtype = 0.5
        self.default_outwav = 'pyjtalk-output.wav'

    def validate_command(self, cmd: Optional[str] = None) -> str:
        """check existance of cmd or fallback to default"""
        # TODO: command validation
        return cmd or self.default_openjtalk_command

    def validate_dictionary(self, dict_path: Optional[str] = None) -> str:
        if dict_path and os.path.isdir(dict_path):
            return dict_path
        else:
            return self.default_dictionary_path


class JTalker(BaseJTalker):
    """Standard JTalker"""

    def talk(
        self,
        context: str,
        openjtalk_command: Optional[str] = None,
        dictionary_path: Optional[str] = None,
        voice_path: Optional[str] = None,
        speed: Optional[float] = None,
        pitch: Optional[float] = None,
        vtype: Optional[float] = None,
        outwav: Optional[str] = None,
    ) -> None:
        """generate wav"""
        # TODO: Validations
        openjtalk_command = self.validate_command(openjtalk_command)
        dictionary_path = dictionary_path or self.default_dictionary_path
        voice_path = voice_path or self.default_voice_path
        speed = speed or self.default_speed
        pitch = pitch or self.default_picth
        vtype = vtype or self.default_vtype
        outwav = outwav or self.default_outwav

        jtalk_cmd = " ".join([
            openjtalk_command,
            "-x", dictionary_path,
            "-m", voice_path,
            "-r", str(speed),
            "-fm", str(pitch),
            "-a", str(vtype),
            "-ow", outwav
        ])

        print("cmd:", jtalk_cmd)
        print("context:", context)
        result = subprocess.run(
            jtalk_cmd,
            shell=True,
            capture_output=True,
            input=context.encode(),
        )
        print(result)


class AsyncJTalker(BaseJTalker):
    """Async JTalker"""
    # TODO: async JTalker
