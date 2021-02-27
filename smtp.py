# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 

  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("ashok.testing12345@gmail.com", "ashok321") 
  
# message to be sent 
message = "testing with smtp"
  
# sending the mail 
s.sendmail("ashok.testing12345@gmail.com", "ashok.venkata1827@gmail.com", message) 
  
# terminating the session 
s.quit() 