import smtplib
import config

#email function
def send_email(subject,msg):
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS,config.PASSWORD)
        subject = "hello"
        msg = "hello"
        message = 'Subject: {}\n\n{}'.format(subject,msg)
        #server.sendmail(config.EMAIL_ADDRESS,config.EMAIL_ADDRESS,message)
        server.sendmail("ashok.testing12345@gmail.com","kakumani_ramesh@hotmail.com",message)
        server.quit()
        print("Sucess")
        return

# main function
subject = "testing with smtp" 
msg = "hi this is ashok"
send_email(subject,msg) 