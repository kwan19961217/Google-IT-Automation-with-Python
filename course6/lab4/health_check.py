#!/usr/bin/env python3
import psutil
import emails
import socket
import time


def cpu_check():
	return psutil.cpu_percent() > 80

def disk_space_check():
	hdd = psutil.disk_usage('/')
	return hdd.free / hdd.total < 0.2

def memory_check():
	ram = psutil.virtual_memory()
	return ram[1] / 1024 ** 2 < 500 

def local_host():
	ip_address = socket.gethostbyname("localhost")
	return ip_address != "127.0.0.1"

sender = "automation@example.com"
recipient = "username@example.com"

error_subject = {
"cpu": "Error - CPU usage is over 80%",
"disk": "Error - Available disk space is less than 20%",
"memory": "Error - Available memory is less than 500MB",
"local_host": "Error - localhost cannot be resolved to 127.0.0.1"
}

body = "Please check your system and resolve the issue as soon as possible."

if cpu_check():
	message = emails.generate_email(sender,recipient,error_subject["cpu"],body)
	emails.send_email(sender, message)

if disk_space_check():
	message = emails.generate_email(sender,recipient,error_subject["disk"],body)
	emails.send_email(sender, message)

if memory_check():
	message = emails.generate_email(sender,recipient,error_subject["memory"],body)
	emails.send_email(sender, message)

if local_host():
	message = emails.generate_email(sender,recipient,error_subject["local_host"],body)
	emails.send_email(sender, message)