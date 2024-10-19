from app.libraries.mail_temp import Mail

if __name__ == '__main__':
    mail = 'isaacperez@cevipsa.com'
    print(Mail.get_mail_link(mail))

