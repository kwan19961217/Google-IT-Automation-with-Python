#!/usr/bin/evn python3

from PIL import Image
import os


path = "./supplier-data/images/"

files = os.listdir(path)
for file in files:
	try:
		im = Image.open(path + image).convert("RGB")
		im.resize((600,400)).save(path + image, "jpeg")
	except:
		print("Not an image file.")