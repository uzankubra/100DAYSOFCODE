import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

# print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()  # **maybe it is a little problem**
price_without_currency = price.split("$")[1]
price_float = float(price_without_currency)
print(price_float)

# send email
import smtplib

title = soup.find(id="productTitle").get_text().strip()
print(title)

price = 200
email="example-smtp-address"
password = "example**"
your_email="kubraauzann@gmail.com"

if price_float < price:
    message = f"{title} is now {price}"

    with smtplib.SMTP(email, port=587) as connection:
        connection.starttls()
        result = connection.login(email, password)
        connection.sendmail(
            from_addr=email,
            to_addrs=your_email,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )