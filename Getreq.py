import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.ebay.com/itm/NEW-ADIDAS-DRAGON-S81906-BLUE-All-Sz-ORIGINALS-CASUAL-SHOES-SNEAKERS/172952542273?_trkparms=aid%3D222007%26algo%3DSIM.MBE%26ao%3D1%26asc%3D47300%26meid%3D5a6bd263b8bb4235983905b0863b06c3%26pid%3D100011%26rk%3D4%26rkt%3D12%26sd%3D201733910856%26itm%3D172952542273&_trksid=p2047675.c100011.m1850")
content = request.content
soup = BeautifulSoup(content,"html.parser")
#<span class="notranslate" id="prcIsum" itemprop="price" style="" content="46.99">US $46.99</span>
element = soup.find("span",{"itemprop":"price","id":"prcIsum","class":"notranslate"})
string_price = element.text.strip()#US $46.99

price_without_symbol = string_price[4:]
price = float(price_without_symbol)

if(price < 50):
	print("you should buy the shoes")
	print("the price of sneakers ${}.".format(price))

else:
	print("It's to expensive")

