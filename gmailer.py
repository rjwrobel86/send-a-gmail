import smtplib

data="bob"
'''
#data = ""
with open('xml-lead.xml', 'r') as file:
    data = str(file.read())
'''

def sendanemail(data):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("USERNAME","PASSWORD")
    server.sendmail(
        "TO_EMAIL",
        "TO_EMAIL_2",
        f" {data} ",

        )
    server.quit()

sendanemail(data)
