#attempt number two. This scrapes all 125 pages and puts the data in three seperate folders. 

from urllib2 import Request, urlopen
from bs4 import BeautifulSoup
import re

prices = []
areas = []
locations = []

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
        areas.append(area)
        
    location_entries = page.find_all("p","address")
    for location in location_entries: 
        locations.append(location.getText())
    