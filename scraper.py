import requests,request
from bs4 import BeautifulSoup
import smtplib
import time
import unicodedata
import math
# URL = 'https://www.amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4R8QGM/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=sony+alpha+ILCE&qid=1563110763&s=gateway&sr=8-5'
URL = 'https://www.amazon.in/Test-Exclusive-646/dp/B07HGJKDRR?smid=A1EWEIV3F4B24B&pf_rd_p=b3b58951-b6e2-415a-a9d8-23dfaefbb2a3&pf_rd_r=VRAF5EERAPNMZ2CWN2SP'

# headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
# headers = request.headers.get('User-Agent')
# request.headers.get('User-Agent')
def check_price():
    page = requests.get(URL)

    soup = BeautifulSoup(page.content,'html.parser')

    # print(soup.prettify())

    title = soup.find(id="productTitle").get_text()

    # print(title.strip())


    price = soup.find(id="priceblock_dealprice").get_text()
    price1 = unicodedata.normalize('NFKD', price).encode('ascii','ignore')
    converted_price1 = int(filter(str.isdigit, price1))
    converted_price = math.floor(converted_price1)/100
    print(price)

    print(converted_price)

    if(converted_price > 17000):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('pricetrackerforall@gmail.com','jjkwdlygrmmraatg')

    subject = "Price Fell Down"
    body = " Hello \n\n Thank you for subscribing at Amazon Price Tracker \n\n The product price is in your budget now \n Check the Amazon link \n " + URL

    # msg = subject + body

    message = 'Subject: {}\n\n{}'.format(subject, body)

    server.sendmail(
        'pricetrackerforall@gmail.com',
        'abhishekmirajkar03@gmail.com',
        message,
    )

    print("Hey Email Has Been Sent")
    # print(msg)

    server.quit()
while(True):
    check_price()
    time.sleep(60)
