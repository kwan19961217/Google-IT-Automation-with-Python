#!/usr/bin/env python3

from PIL import Image
import os


path = "./supplier-data/images/"

files = os.listdir(path)
for file in files:
	try:
		f, e = os.path.splitext(file)
		im = Image.open(path + file).convert("RGB")
		im.resize((600,400)).save(path + f +".jpeg")
	except:
		print("Not an image file.")