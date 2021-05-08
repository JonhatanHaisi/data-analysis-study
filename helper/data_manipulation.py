# -*- coding: UTF-8 -*-

from zipfile import ZipFile
from pathlib import Path

def unzip(file, output_path):
    Path(output_path).mkdir(parents=True, exist_ok=True)
    
    with ZipFile(file, 'r') as file:
        file.extractall(output_path)