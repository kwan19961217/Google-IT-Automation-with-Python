#!/usr/bin/env python3
import os
import datetime
import reports

if __name__ == "__main__":
	path = "./supplier-data/descriptions/"
	files = os.listdir(path)
	content = ""
	today = datetime.datetime.today()

	for file in files:
		with open(path + file) as f:
			rows = f.readlines()
			temp = f"name: {rows[0]}\nweight: {rows[1]}\n"
			content += temp

	reports.generate_report("/tmp/processed.pdf", f"Processed Update on {today}", content)