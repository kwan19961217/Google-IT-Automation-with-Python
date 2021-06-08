#!/usr/bin/env python3
import os
import datetime
import reports
import emails


if __name__ == "__main__":
	path = "./supplier-data/descriptions/"
	files = os.listdir(path)
	content = ""
	today = datetime.datetime.today()
	report_path = "/tmp/processed.pdf"

	for file in files:
		with open(path + file) as f:
			rows = f.readlines()
			temp = f"name: {rows[0]}\nweight: {rows[1]}\n"
			content += temp

	reports.generate_report(report_path, f"Processed Update on {today}", content
	message = emails.generate_email("automation@example.com", "username@example.com", 
							"Upload Completed - Online Fruit Store", 
							"All fruits are uploaded to our website successfully. A detailed list is attached to this email.", 
							report_path)
	emails.send_email("automation@example.com", message)
