import asyncio
import logging
import os
import subprocess
from typing import Optional

from .config import PYJTALK_DEFAULT_DICTIONARY_PATH, PYJTALK_DEFAULT_VOICE_PATH

logger = logging.getLogger(__name__)

DEFAULT_FILE_NAME = 'pyjtalk.wav'


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
        self.default_outwav = '/dev/stdout'

        # TODO: Validate result cache (may require new class...?)

    def validate_command(self, cmd: Optional[str] = None) -> str:
        """check existance of cmd or fallback to default"""
        # TODO: command validation
        return cmd or self.default_openjtalk_command

    def validate_dictionary(self, dict_path: Optional[str] = None) -> str:
        if dict_path and os.path.isdir(dict_path):
            return dict_path
        else:
            return self.default_dictionary_path

    def construct_command(
        self,
        openjtalk_command: Optional[str] = None,
        dictionary_path: Optional[str] = None,
        voice_path: Optional[str] = None,
        speed: Optional[float] = None,
        pitch: Optional[float] = None,
        vtype: Optional[float] = None,
        outwav: Optional[str] = None,
    ) -> str:
        # TODO: Validations
        openjtalk_command = self.validate_command(openjtalk_command)
        dictionary_path = dictionary_path or self.default_dictionary_path
        voice_path = voice_path or self.default_voice_path
        speed = speed or self.default_speed
        pitch = pitch or self.default_picth
        vtype = vtype or self.default_vtype
        outwav = outwav or self.default_outwav

        return " ".join([
            openjtalk_command,
            "-x", dictionary_path,
            "-m", voice_path,
            "-r", str(speed),
            "-fm", str(pitch),
            "-a", str(vtype),
            "-ow", outwav
        ])


class JTalker(BaseJTalker):
    """Standard JTalker"""

    def synthesize(
        self,
        context: str,
        ** kwargs,
    ) -> bytes:
        """_summary_

        Args:
            context (str): _description_

        Raises:
            RuntimeError: _description_

        Returns:
            Optional[bytes]: _description_
        """
        jtalk_cmd = self.construct_command(**kwargs)
        logger.debug("cmd: " + jtalk_cmd)
        logger.debug("context: " + context)

        result = subprocess.run(
            jtalk_cmd,
            shell=True,
            capture_output=True,
            input=context.encode(),
        )

        if result.returncode != 0:
            logger.critical(result.stderr)
            raise RuntimeError("openjtalk command failed")

        return result.stdout

    def synthesize_wav(
        self,
        context: str,
        filename: str = DEFAULT_FILE_NAME,
        **kwargs
    ) -> None:
        stdout = self.synthesize(context, **kwargs)

        with open(filename, mode='bw') as f:
            f.write(stdout)


class AsyncJTalker(BaseJTalker):
    """Async JTalker"""
    async def synthesize(
        self,
        context: str,
        ** kwargs,
    ) -> bytes:
        jtalk_cmd = self.construct_command(**kwargs)
        logger.debug("cmd: " + jtalk_cmd)
        logger.debug("context: " + context)

        sp = await asyncio.subprocess.create_subprocess_shell(
            jtalk_cmd,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        stdout_data, stderr_data = await sp.communicate(input=context.encode())

        if sp.returncode != 0:
            logger.critical(stderr_data)
            raise RuntimeError("openjtalk command failed")

        return stdout_data

    async def synthesize_wav(
        self,
        context: str,
        filename: str = DEFAULT_FILE_NAME,
        **kwargs
    ) -> None:
        stdout = await self.synthesize(context, **kwargs)

        with open(filename, mode='bw') as f:
            f.write(stdout)
