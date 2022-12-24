
#improting necessary libraries



from bs4 import BeautifulSoup
import requests
from requests import get
import time
import random


count = 1
url = 'https://www.avito.ru/moskva?p='+str(count)+'&q=iphone+13+pro+256+gb'                                               #avito url, here we divide it into 2 str to increment page counter
                                                                                                                         # on avito current page apear at url at symbol 'p='


iphones = []                                                                                                             #creating the empty list to store our info


while count <50:                                                                                                         #3 is how many pages                                                                 #creating loop to search through pages
    time.sleep(2)
    url = 'https://www.avito.ru/moskva?p=' + str(count) + '&q=iphone+13+pro+256+gb'
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')                                                               #reading the html page
    iphone_data = html_soup.find_all('div', class_='iva-item-content-rejJg')                                            #finding all info in each cards on avito
    if iphone_data != []:
        iphones.extend(iphone_data)                                                                                      #if we see some info then we save all(and fresh cards still exist)
        value = random.random()
        scaled_value = 1 + (value * (5))
        print(scaled_value)
        time.sleep(scaled_value)                                                                                          #pauses our program to avoid ban
    else:
        print('empty!')
        break
    count +=1

#print (len(iphones))                                                                                                     #how much we find
#print(iphones[1])
#print()

n = int(len(iphones)-1)
counter = 0
print(iphones)
while counter < 5 :                                                                                                       #actually u can go to n(all you find
    info = iphones[int(counter)]
    prize = info.find('h3 itemprop="name" ',{"class":"title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH text-text-LurtD text-size-s-BxGpL text-bold-SinUO"}).text
    title = info.find('span',{"class":"price-text-_YGDY text-text-LurtD text-size-s-BxGpL"}).text
    print(title, ' ', prize)
    counter +=1





