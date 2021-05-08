# -*- coding: UTF-8 -*-

import requests

from .utils import mkdir

def from_url(url, output_path='./data'):
    mkdir(output_path)
    
    response = requests.get(url)
    file_name = url.split("/")[-1]
    
    with open(f"{output_path}/{file_name}", 'wb') as f:
        f.write(response.content)

