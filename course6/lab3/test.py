from email.message import EmailMessage
message = EmailMessage()
sender = "me@example.com"
recipient = "you@example.com"
message["From"] = sender
message["To"] = recipient
print(message)

print(inch)