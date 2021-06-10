#!/usr/bin/env python3
import os
import requests
import re


url = "http://IP Address/fruits/"
path ="./supplier-data/descriptions/"

files = os.listdir(path)
for file in files:
	if file.endswith(".txt"):
		with open(path + file) as f:
			rows = f.readlines()
			weight = re.match(r"[\d]+", rows[1])[0]
			requests.post(url, json={
				"name": rows[0],
				"weight": weight,
				"description": rows[2]": 
				"image_name": file[:-4] + ".jpeg"})
