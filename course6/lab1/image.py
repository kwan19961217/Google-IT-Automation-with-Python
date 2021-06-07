#!/usr/bin/python3

from PIL import Image
import os
from pathlib import Path


Path("/opt/icons/").mkdir(parents=True, exist_ok=True)

files = os.listdir("./images/")

for file in files:
        try:
                im = Image.open("./images/" + file).convert('RGB')
                im.resize((128,128)).rotate(90).save("/opt/icons/" + file, "jpeg")
        except:
                print("Skipping unrelated files")