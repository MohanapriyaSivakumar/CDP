#!/usr/bin/env python
# coding: utf-8

# # Newspaper scraping
# 
# ## Imposing  structure on data
# 
# * Web scraping focuses on the transformation of unstructured data on the web
# * Typically in html format, into structured data that can be stored
# * And analyzed in a central local database or spreadsheat
# 
# ![](../images/web2.jpg)
# 
# here we consider the UK BBC News website i.e https://www.bbc.co.uk/search?q=covid+19&page=1 and searched about covid 19 in a search box present on the top of the page shown in the picture.
# 
# ![](../images/web3.png)
# 
# 
# 
# Let we write the script to scrape the news by giving keywords in our python
# 
# ## Import the packages
# 
# here the the BBC news website had written using html scripts to extract the html scripts we have to install the BeautifulSoup and requests packages.

# In[1]:


import urllib.request,sys,time
from bs4 import BeautifulSoup
import requests
import pandas as pd


# ## pages to get
#  After searching of keywords the results shown in the number of pages
# 
# ![](../images/web4.png)
# 
# so we have to intialize the variable to request the particular page and the result of the searching will be stored in the dataframe. 
# 
# 

# In[2]:


pagesToGet= 1
resultframe=[]


# ## get the keyword to search

# In[6]:


key=input("Enter the query: ")
key=key.replace(' ','+')
print(key)


# ## Extracting html script
# write the code to extract html script using class names mentioned in the bbc news website.
# 
# ![](../images/web5.png)
# 
# and the result stored in the csv file named <b>"search_res.csv" </b>

# In[9]:


for page in range(1,pagesToGet+1):
    print('processing page :', page)
    url = 'https://www.bbc.co.uk/search?q='+key+'+article&page='+str(page)
    print(url)
    page=requests.get(url)            
    soup=BeautifulSoup(page.text,'html.parser')
    frame=[]
    links=soup.find('ul',attrs={'class':'css-1lb37cz-Stack e1y4nx260'}).find_all('li')
    #links=soup.find_all('li',attrs={'class':'o-listicle__item'})
    print(len(links))
    filename="search_res.csv"
    f=open(filename,"w", encoding = 'utf-8')
    headers="Statement,Link,Date\n"
    f.write(headers)
    
    for j in links:
      
        Statement = j.find("div",attrs={'class':'css-l100ew-PromoContentSummary e1f5wbog1'}).find('p',attrs={'class':'css-1uw1j0b-PromoHeadline e1f5wbog2'}).find('a',attrs={'class':'css-vh7bxp-PromoLink e1f5wbog6'}).text.strip()
       
        Link = j.find("p",attrs={'class':'css-1uw1j0b-PromoHeadline e1f5wbog2'}).find('a')['href'].strip()
        Date = j.find('span',attrs={'class':'css-1hizfh0-MetadataSnippet ecn1o5v0'}).text[8:].strip()
       
        frame.append((Statement,Link,Date))
        f.write(Statement.replace(",","^")+","+Link+","+Date.replace(",","^")+"\n")
    resultframe.extend(frame)
f.close()


# ## Result csv file
# 
# here in a page there are 10 links are displayed. The title of the news related to keyword and published url and published date are stored in the csv file.

# In[12]:


data=pd.DataFrame(resultframe, columns=['Statement','Link','Date'])
print(data)


# ## using Article package
# 
# using the article package, we can display the various properties of news article like title of the news, summary of the news, meta description etc., we can take the link of the above result i.e data DataFrame.

# In[13]:


data['Link']


# ### installing the package

# In[15]:


get_ipython().system('pip install newspaper3k')


# ### importing the package

# In[16]:


from newspaper import Article 


# In[17]:


url = data['Link'][1] #for example take a first result link


# ### apply parsing to know the properties of news article easily

# In[19]:


res_article = Article(url, language="en") # en for English 
res_article.download()  #download an article
res_article.parse() #To parse the article 
res_article.nlp() #To perform natural language processing ie..nlp 


# ### displaying the title of the news article

# In[23]:


res_article.title


# ### displaying the text of the news article

# In[24]:


res_article.text


# ### using BeautifulSoup to extract entire article

# In[25]:


url=data['Link'][2]
url


# ![](../images/web6.png)

# In[26]:


page=requests.get(url)
     
soup=BeautifulSoup(page.text,'html.parser')
frame=[]
links=soup.find('article',attrs={'class':'css-5h7eao-ArticleWrapper e1nh2i2l0'}).find_all('div',attrs={'class':'css-uf6wea-RichTextComponentWrapper e1xue1i83'})
#links=soup.find_all('li',attrs={'class':'o-listicle__item'})
#print("l:"+links)
for i in links:
    news=i.find('div',attrs={'class':'css-83cqas-RichTextContainer e5tfeyi2'}).text
    print(news)


# In[ ]:




