#!/usr/bin/env python
# coding: utf-8

# # Mapping using Python
# 
# Here we use geotext library to extract places names from the sentence.
# 
# ## Installation of geotext modules

# In[1]:


get_ipython().system('pip install geotext')


# ### Example to use GeoText module

# In[2]:


from geotext import GeoText

places = GeoText("I was in Chennai on that day and next day i went to Erode")
places.cities


# ## Example to Exract place names from a website
# 
# * here we going to extract place names from the caption of the picture on the site , "https://www.gutenberg.org/files/64316/64316-h/64316-h.htm"
# 
# * also we used the method of previous web scraping method using BeautifulSoup module
# 
# 
# ![](../images/map2.png)

# In[3]:


import urllib.request,sys,time
from bs4 import BeautifulSoup
import requests
import pandas as pd
from geotext import GeoText


# In[13]:


url="https://www.gutenberg.org/files/64316/64316-h/64316-h.htm"


# In[266]:


page=requests.get(url)
     
soup=BeautifulSoup(page.text,'html.parser')
frame=[]
resultframe=[]
links=soup.find_all('div',attrs={'class':'ills'})
#links=soup.find_all('li',attrs={'class':'o-listicle__item'})
#print(links)
filename="caption.csv"
f=open(filename,"w", encoding = 'utf-8')
headers="Link,Caption\n"
f.write(headers)
u='https://www.gutenberg.org/files/64316/64316-h/'
for i in links:
    k=i.find_all('div',attrs={'class':'figcenter'})
    for j in k:
        l=j.find_all('a')
        Link = u+l[1].find('img')['src'].strip()          #Extract Link of all the images
        cap=j.find('p',attrs={'class':'caption'}).text.strip()  #Extract caption of all the images
        
        
        a=cap.replace(' ',',').title()

        result = GeoText(a,'US').cities
        
        if(result!=[]):
            frame.append((Link,str(result[0])))  
            f.write(Link+","+str(result[0])+"\n")   #stored only the link and caption that contains city names
    resultframe.extend(frame)
f.close()
        


# ### Result of the above Code

# In[14]:


data=pd.DataFrame(resultframe, columns=['Link','Caption'])
print(data)


# ### Installing arcgis to map the places

# In[214]:


get_ipython().system('pip install arcgis')


# ## Code to find latitude and longitude
# here we find the latitude and longitude of the places that extract in the caption of the images. and we mark the point on the map using simple loop condition. 

# In[16]:


from arcgis.gis import GIS
from arcgis.geometry import Point
from arcgis.geocoding import geocode, reverse_geocode

my_gis = GIS()
# m = my_gis.map()

m = my_gis.map("US", zoomlevel=4)


# function to find the latitude and longitude
def place_names(get_places):
    i=get_places
    geocoded=geocode(i)[0]['location']
    return geocoded

for i in data['Caption']:

    geocoded=place_names(i)
    lat=geocoded['y']
    longi=geocoded['x']
    print(lat,longi)
    
    location = {
     'Y': lat,                 # `Y` is latitude
     'X':  longi,               # `X` is longitude
     'spatialReference': {
         'wkid':4326
     }
    }
    unknown_pt = Point(location)
    address = reverse_geocode(location=unknown_pt)
    print(address)  #matching address found from the latitude and longitude
   
    m.draw(address)
  
   


# ### Result Map of the above code

# In[17]:


m


# ![](../images/resmap1.png)

# ## Example to Find the address of the Given latitude and longitude

# In[19]:


from arcgis.geometry import Point
location = {
     'Y': 39.86347000000006,                 # `Y` is latitude
     'X':  -105.05000999999999,               # `X` is longitude
     'spatialReference': {
         'wkid':4326
     }
}
unknown_pt = Point(location)
address = reverse_geocode(location=unknown_pt)
address


# ### Draw a map for above address

# In[21]:


m = my_gis.map("USA", zoomlevel=5)
m.draw(address)
m


# ![](../images/resmap2.png)

# ## map can be save as html file

# In[22]:


file_path = r"C:\Users\Mohanapriya\city_map.html"
m.export_to_html(file_path)


# In[333]:


import webbrowser
webbrowser.open_new('http://127.0.0.1:2000/')

