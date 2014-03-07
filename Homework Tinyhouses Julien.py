from urllib2 import Request, urlopen
from urllib import urlretrieve
from bs4 import BeautifulSoup
import re

#tried this first, don't understand why it didn't work / I'm not sure I understand how find_all works

for i in range(125):
    
    url = "http://tinyhouselistings.com/page/"+str(i+1)+"/?s=all+properties&amp;search=search&amp;srch_type&amp;srch_location&amp;srch_area&amp;srch_price&amp;srch_keyword&amp;srch_bedrooms&amp;srch_bathroom"
    
    request = Request(url)
    
    request.add_header('From',"jag2296@columbia.edu")
    
    connection = urlopen(request)
    
    data = connection.read()
    
    page = BeautifulSoup(data)
    pages.append(page)

prices = []  

for page in pages:
    text=page.find_all("span","price")
    prices.append(text.getText())

area = []

for page in pages:
    text=page.find_all("Sq","Ft")
    area.append(text.getText())

location = []
for page in pages:
    text=page.find_all("span","adress")
    prices.append(text.getText())

# second attempt 

prices = []
surface = []
location = []

for i in range(125):
    
    url = "http://tinyhouselistings.com/page/"+str(i+1)+"/?s=all+properties&amp;search=search&amp;srch_type&amp;srch_location&amp;srch_area&amp;srch_price&amp;srch_keyword&amp;srch_bedrooms&amp;srch_bathroom"
    
    request = Request(url)
    
    request.add_header('From',"jag2296@columbia.edu")
    
    connection = urlopen(request)
    
    data = connection.read()
    
    page = BeautifulSoup(data)
    
    price_entries = page.find_all("span","price")
    
    for price in price_entries: 
        prices.append(price.getText())
        area = price.find_next(text=re.compile("Sq\. Ft\."))
        surface.append(area)
        location = price.find_next(text=re.compile("address*."))

len(prices), len(area), len(location)

#the location part doesn't work



#let's look at the mistakes
from pandas import read_csv
urlretrieve("http://compute-cuj.org/mistakes.csv","mistakes.csv")
mistakes = read_csv("mistakes.csv")
mistakes 

#let's get the price data
urlretrieve("http://compute-cuj.org/pricedata.csv","pricedata.csv")
pricedata = read_csv("pricedata.csv")
pricedata

#I don't think this does what we want it to do / I don't really understand matplotlib

from matplotlib import pyplot as PLT
import numpy as np

with open('pricedata.csv') as f:
  v = np.loadtxt(f, delimiter=",", dtype='float', comments="#", skiprows=1, usecols=None)

v_hist = np.ravel(v)   
fig = PLT.figure()
ax1 = fig.add_subplot(111)

n, bins, patches = ax1.hist(v_hist, bins=50, normed=1, facecolor='green')
PLT.show()


#other methods return "AttributeError: max must be larger than min in range parameter."

from matplotlib import pyplot as PLTimport numpy as np 

fig = PLT.figure()
ax1 = fig.add_subplot(111)
PLT.hist(prices, bins=100)
PLT.ylabel('price')
PLT.title("Price of Tiny Houses")

plt.show()


