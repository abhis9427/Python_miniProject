# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import smtplib

url = 'https://www.flipkart.com/realme-narzo-10a-so-blue-32-gb/p/itmbeb412dade152?pid=MOBFQ36AYV4ZG4E4&lid=LSTMOBFQ36AYV4ZG4E4LAVPVB&marketplace=FLIPKART&srno=b_1_1&otracker=hp_reco_Top%2BSelection_3_8.dealCard.OMU_Top%2BSelection_cid%3AS_F_N_tyy_4io__bs___NONE_ALL%3Bnid%3Atyy_4io_%3Bet%3AS%3Beid%3Atyy_4io_%3Bmp%3AF%3Bct%3Ab%3B_5&otracker1=hp_reco_WHITELISTED_personalisedRecommendation%2FC6_Top%2BSelection_DESKTOP_HORIZONTAL_dealCard_cc_3_NA_view-all_5&fm=personalisedRecommendation%2FC6&iid=c91dfe84-30ce-4ae5-8b4b-713741ca4141.MOBFQ36AYV4ZG4E4.SEARCH&ppt=browse&ppn=browse&ssid=5n2ca9akkw0000001592251041136'
headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

def send_mail():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  #server.connect("smtp.gmail.com",587)
  server.ehlo()
  server.starttls()
  server.ehlo()
  server.login('from_example@gmail.com','password')
  subject = 'IT IS A TEST MAIL'
  body = 'Check the Flipkart Link : url= https://www.flipkart.com/realme-narzo-10a-so-blue-32-gb/p/itmbeb412dade152?pid=MOBFQ36AYV4ZG4E4&lid=LSTMOBFQ36AYV4ZG4E4LAVPVB&marketplace=FLIPKART&srno=b_1_1&otracker=hp_reco_Top%2BSelection_3_8.dealCard.OMU_Top%2BSelection_cid%3AS_F_N_tyy_4io__bs___NONE_ALL%3Bnid%3Atyy_4io_%3Bet%3AS%3Beid%3Atyy_4io_%3Bmp%3AF%3Bct%3Ab%3B_5&otracker1=hp_reco_WHITELISTED_personalisedRecommendation%2FC6_Top%2BSelection_DESKTOP_HORIZONTAL_dealCard_cc_3_NA_view-all_5&fm=personalisedRecommendation%2FC6&iid=c91dfe84-30ce-4ae5-8b4b-713741ca4141.MOBFQ36AYV4ZG4E4.SEARCH&ppt=browse&ppn=browse&ssid=5n2ca9akkw0000001592251041136'
  msg = f"{subject}\n\n{body}"
  server.sendmail(
      'From_example@gmail.com',
      'To_example@gmail.com',
      msg
  )
  print('EMAIL SENT')
  server.quit()

page = requests.get(url, headers = headers)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find("span", {"class" : "_35KyD6"}).get_text()
price = soup.find("div", {"class": "_1vC4OE _3qQ9m1"}).get_text().replace(',','')
converted_price = float(price[1:5])

print(title)
print(converted_price)
if(converted_price<8000):
  send_mail()