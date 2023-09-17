import requests
from bs4 import BeautifulSoup
import time

cryptosearch = input("Enter currency: ")
urlbtc = "https://arzdigital.com/coins/bitcoin/"
dollarurl = "https://irarz.com/"
responsedollar = requests.get(url=dollarurl)
responsedollartxt = responsedollar.text
soupdollar = BeautifulSoup(responsedollartxt, "html.parser")
dollar = soupdollar.find("span", id="usdmax")
dollarprice = dollar.text
english_dollar = dollarprice.replace("۰", "0").replace("۱", "1").replace("۲", "2").replace("۳", "3").replace("۴", "4").replace("۵", "5").replace("۶", "6").replace("۷", "7").replace("۸", "8").replace("۹", "9")
english_dollarr = dollarprice.replace(",", "").replace("۰", "0").replace("۱", "1").replace("۲", "2").replace("۳", "3").replace("۴", "4").replace("۵", "5").replace("۶", "6").replace("۷", "7").replace("۸", "8").replace("۹", "9")

try:
    if cryptosearch == "btc":
        resbtc = requests.get(url=urlbtc)
        resbtctxt = resbtc.text
        soupbtc = BeautifulSoup(resbtctxt, 'html.parser')
        btcusdt = soupbtc.find("div", class_="arz-coin-page-data__coin-price coinPrice btcprice pulser")
        btcprice = "BTC Price: " + btcusdt.text
        nagoo = btcusdt.text
        print(btcprice)
        btcpricee = nagoo.replace(",", "").replace("$", "")
        nasa2 = float(english_dollarr) * float(btcpricee)
        print(f"{cryptosearch} in IR:", nasa2, "Rials")
    else:
        url = f"https://arzdigital.com/coins/{cryptosearch}/"
        response = requests.get(url=url)
        responsetxt = response.text
        soup = BeautifulSoup(responsetxt, "html.parser")
        usdt = soup.find("div", class_="arz-coin-page-data__coin-price coinPrice pulser")
        price = f"{cryptosearch} Price: " + usdt.text
        zza = usdt.text
        print(price)
        usdtpricee = zza.replace(",", "").replace("$", "")
        nasa1 = float(english_dollarr) * float(usdtpricee)
        print(f"{cryptosearch} in IR:", nasa1, "Rials")
    print("Dollar price in IR:", english_dollar, "Rials")
    time.sleep(100)
except:
    print("Please enter valid crypto currency.")
    time.sleep(10)

