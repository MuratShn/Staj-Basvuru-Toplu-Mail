import time
import random
import requests
from bs4 import BeautifulSoup as bs

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}


emails = []


"""url = "https://www.yildizteknopark.com.tr/tr/firma-goruntule/3"
response = requests.get(url,headers=headers)
soup = bs(response.content,"html.parser")
a = soup.find("div",{"class":"boxes"}).find_all("a")
a[1].text"""


for i in range(221,421): ##1-221   221-421
    
    if  i%20==0:
        time.sleep(random.randint(10,30))
    
    url = f"https://www.yildizteknopark.com.tr/tr/firma-goruntule/{i}"
    response = requests.get(url,headers=headers)
    soup = bs(response.content,"html.parser")
    a = soup.find("div",{"class":"boxes"}).find_all("a")
    if(a[1].text == " "):
        continue
    else:
        emails.append(a[1].text)
    print(i)
    
with open("emailler.txt","a",encoding="utf-8")as file:
    for i in emails:
        file.write(i+"\n")
