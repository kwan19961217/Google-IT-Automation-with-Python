#!/usr/bin/env python3
import os
import requests

url = "IP Address"
path ="./supplier-data/description/"

files = os.listdir(path)
for file in files:
	if file.endwswith(".txt"):
		with open(file) as f:
			rows = f.readlines()
			requests.post(url, files={
				"name": rows[0],
				"weight": rows[1],
				"description": rows[2]": 
				"image_name": file[:-3] + ".jpeg"})
