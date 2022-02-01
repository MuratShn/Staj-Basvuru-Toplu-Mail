from email import policy
from email.message import EmailMessage
from email.mime.application import MIMEApplication
import random
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time


emails = []
sayac = 0

with open("emailler.txt","r+",encoding="utf-8") as file:
    for i in file.readlines():
        try:
            if sayac%5==0:
                time.sleep(random.randint(10,20))
                
            i = i.strip("  \n")

            sender = "muratsahh.37@gmail.com"

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()

            server.login(sender,"Şifre")
            msg = MIMEMultipart()
            
            msg["From"] = "muratsahh.37@gmail.com"  # kımden gıdıcegını yazıyoruz
            msg["To"] = f"{i}"  # kıme gonderıcegın
            msg["Subject"] ="Stajyer Başvuru"  # mail baslık  kısmı

            yazı = """

		İçerik Metni
            """

            mesaj_govdesi = MIMEText(yazı,"plain")
            msg.attach(mesaj_govdesi)

            with open("cv.pdf","rb") as f:
                attach = MIMEApplication(f.read(),_subtype="pdf") #pdf ekleme

            attach.add_header('Content-Disposition','attachment',filename=str("cv.pdf")) #pdf ekleme 
            msg.attach(attach)
            server.send_message(msg)
            print(f"gitti ///   {sayac}")
            sayac+=1
        except Exception as e:
            print(f"Kalınan Mail: :{i}     {sayac}")
            print(e)



