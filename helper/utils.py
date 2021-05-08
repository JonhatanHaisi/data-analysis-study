# -*- encode: utf-8 -*-

from pathlib import Path

def mkdir(directory):
    Path(directory).mkdir(parents=True, exist_ok=True)
