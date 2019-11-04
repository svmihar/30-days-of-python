#!/usr/bin/env python

import requests
from tqdm import tqdm

shakespeare = open("shakespeare.txt").read().splitlines()

for text in tqdm(shakespeare):
    requests.get(f"http://127.0.0.1:5000/task?n={text}")
