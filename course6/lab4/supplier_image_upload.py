#!usr/bin/env python3
import requests
import os

url = "IP Address"
path = "./supplier/images/"

files = os.listdir(path)
for file in files:
	if file.endswith(".jpeg"):
		with open(path + file, "rb") as f:
			requests.post(url, files={"file": f})