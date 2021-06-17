from bs4 import BeautifulSoup
import requests
import time
import matplotlib.pyplot as plt

URL = "https://finance.yahoo.com/quote/AMD"


for i in range(3):
    html_text = requests.get(URL).text
    soup = BeautifulSoup(html_text,'lxml')
    company_name = soup.find('h1',class_="D(ib) Fz(18px)").text 
    share_price = soup.find('span',class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").text
    
    time_stamp =  (soup.find('div',class_ = "C($tertiaryColor) D(b) Fz(12px) Fw(n) Mstart(0)--mobpsm Mt(6px)--mobpsm")).span.text
    print(f"{company_name} share costs {share_price} {time_stamp} \n")

#plt.plot(share_price)
#plt.show()
