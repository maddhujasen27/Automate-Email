import smtplib
import getpass

sender_email = 'xyz@gmail.com'
receiver = ['abc@gmail.com' , 'def@gmail.com']
password = getpass.getpass('Enter your password')
subject = 'Hello There'
body = 'How you doin ?'
message = f'Subject: {subject}\n\n{body}'
server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login(sender_email,password)
print("Login successful")
for i in range(50) :
    server.sendmail(sender_email,receiver,message)

print("Sent")
