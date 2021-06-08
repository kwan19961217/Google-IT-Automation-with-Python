#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import datetime
import os


def generate_report(files):
	path = "./supplier-data/descriptions/"
	files = os.listdir(path)
	
	report = SimpleDocTemplate("processed.pdf")
	styles = getSampleStyleSheet()
	report_title = Paragraph("Processed Update On {}".format(datetime.datetime.today()))
	line_break = Spacer(1, 2*inch)
	report_content = [report_title]
	for file in files:
		with open(path + file) as f:
			rows = f.readlines()
			report_content.append(line_break)
			report_content.append(rows[0])
			report_content.append(rows[1])
	report.build(report_content)
