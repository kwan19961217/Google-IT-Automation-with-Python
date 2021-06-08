#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


def generate_report(attachment, title, content):
	report = SimpleDocTemplate(attachment)
	styles = getSampleStyleSheet()
	report_title = Paragraph(title)
	line_break = Spacer(1, 2*inch)
	report.build([report_title, line_break, content])