#Q5:-
import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey='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')
from_email = Email("akshitasharma01111@gmail.com")
to_email = Email("gouravsareen0112@gmail.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
