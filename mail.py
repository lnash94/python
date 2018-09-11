import smtplib

content="sample email stuff here "
server = smtplib.SMTP('smtp.gmail.com',587)

server.ehlo()

server.starttls()


#login to the server

server.login("lnash94.nk@gmail.com","1994@Sum")

#send email

server.sendmail("lnash94.nk@gmail.com","sumudunissanke@gmail.com",content)

server.close()


