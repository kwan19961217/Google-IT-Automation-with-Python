#!/usr/bin/env python3

import os
import requests

path = "/data/feedback/"

files = os.listdir(path)
for file in files:
        if file.endswith(".txt"):
                with open(path + file) as f:
                        content = f.readlines()
                        user_input = {
                        "title": content[0].strip(),
                        "name": content[1].strip(),
                        "date": content[2].strip(),
                        "feedback": content[3].strip()
                        }
                        response = requests.post("http://<url>/feedback/", json=user_input)
                        print(response.request.body)
                        response.raise_for_status()