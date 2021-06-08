#!/usr/bin/env python3
import os
import requests
import re


url = "IP Address"
path ="./supplier-data/description/"

files = os.listdir(path)
for file in files:
	if file.endwswith(".txt"):
		with open(file) as f:
			rows = f.readlines()
			weight = re.match(r"[\d]+", rows[1])[0]
			requests.post(url, json={
				"name": rows[0],
				"weight": weight,
				"description": rows[2]": 
				"image_name": file[:-4] + ".jpeg"})
