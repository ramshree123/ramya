# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
 
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("ramyashreesuresh57@gmail.com", "saraswathi")
 
# message to be sent
message = "hello"
 
# sending the mail
s.sendmail("ramyashreesuresh57@gmail.com", "ramyashreesuresh57@gmail.com", message)
print("yaa")
# terminating the session
s.quit()
