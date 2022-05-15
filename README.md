# PyJTalk

OpenJTalk Wrapper for Python.

Simply calling `open_jtalk` command via python's `subprocess`

Async API is available with `AsyncJTalker`.

## Use with `docker-compose`

### Requirements

* Docker
* docker-compose
* The Internet connection

### Usage

`docker-compose run --rm pyjtalk "これはテストです"`

## Use with Python code

### Requirements

* Python
* `open_jtalk` command
* Dictionary file for OpenJTalk
* Voice Model file for OpenJTalk (`*.htsvoice`)

### Install

```sh
# Use pip
pip install git+https://github.com/alcnaka/pyjtalk
```

### Usage

```python
from pyjtalk.jtalker import JTalker

jtalker = Jtalker(
    default_dictionary_path="/usr/share/open_jtalk/voices/mei/mei_normal.htsvoice",
    default_voice_path="/var/lib/mecab/dic/open-jtalk/naist-jdic/",
)

# Get bytes with *.wav format.
voice_bytes = jtalker.synthesize("こんにちは")

# Generate .wav file
voice_bytes = jtalker.synthesize_wav("こんにちは", filename="outfile.wav")
```

## Config

### Environment Variables

```txt
PYJTALK_DEFAULT_VOICE_PATH
Default: "/usr/share/open_jtalk/voices/mei/mei_normal.htsvoice"

PYJTALK_DEFAULT_DICTIONARY_PATH
Default: "/var/lib/mecab/dic/open-jtalk/naist-jdic/"

## Debug

`docker-compose run --rm --entrypoint "bash" pyjtalk`
