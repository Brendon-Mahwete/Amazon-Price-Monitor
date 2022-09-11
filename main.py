#This program gets the price  of a product on amazon using the link of the product.
from bs4 import BeautifulSoup
import lxml
import requests
import smtplib

#The url of the amazon product
URL = "https://www.amazon.com/PlayStation-DualSense-Wireless-Controller-Midnight-5/dp/B094WL86N5/ref=lp_16225016011_1_12"

#Header to bypass the amazon securities, these can be obtained at http://myhttpheader.com/
headers = {
    "User-Agent": "***********************",
    "Accept-Language": "*******************"
           }

#Getting the amazon html detail using requests and BeautifulSoup
results = requests.get(url=URL, headers=headers)
results.raise_for_status()
soup_me = results.text
soup = BeautifulSoup(soup_me, "lxml")

#Getting the the that has the price of the product
price = soup.find("span", class_="a-price-whole")
cents = soup.find("span", class_="a-price-fraction")
amount = float(f"{price.text}{cents.text}")

print(f"The price of the product is ${amount}")

#-----------------------------------------------------Sending an email------------------------------------------------
#The target of the we want
target = 50

#The receivers email
email_to = "bmjay465@gmail.com"

#The senders email details
my_email = "mjaybren@yahoo.com"
password = "******************"

# Checking if the price is lower or equal to the target price, if it is then an email will be sent
if amount <= target:
    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=email_to,
                            msg=f"Subject: Amazon Product alert\n\nThe product is below your target price."
                                f"\n\nclick to purchase {URL}")
        connection.quit()

