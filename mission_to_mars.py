#!/usr/bin/env python
# coding: utf-8

# In[3]:


from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser


# In[34]:


path = {'executable_path': '/Users/users/opt/chromedriver_1'}


# In[36]:


browser = Browser('chrome', **path, headless=False)


# In[28]:


url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"


# In[ ]:


link_answer = requests.get(url)


# In[29]:


soup_handler = bs(link_answer.text, 'html.parser')


# In[31]:


browser_ = driver.get('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')


# In[41]:


img_link = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"


# In[42]:


browser.visit(img_link)


# In[43]:


browser_html = browser_.html
browse_soup = bs(browser_html, 'html.parser')


# In[44]:


img_get = requests.get(img_link)


# In[45]:


soup_image = bs(img_get.text, 'html.parser')


# In[68]:


img_query = soup_image.find_all('a', class_= '')


# In[ ]:


print(img_query)


# In[22]:


title = soup_handler.title.text


# In[24]:


paragraph = soup_handler.p.text


# In[23]:


title_ = print(title)


# In[25]:


paragraph_ = print(paragraph)


# In[ ]:


featured_image_url = "https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA23929_hires.jpg"


# In[70]:


twitter_url = "https://twitter.com/marswxreport?lang=en"


# In[71]:


twitter_answer = requests.get(twitter_url)


# In[72]:


soup_twitter_object = bs(twitter_answer.text, 'html.parser')


# In[ ]:


print(soup_twitter_object.prettify())


# In[1]:


weather_on_mars = 'sol 530 (2020-05-23) low -92.6ºC (-134.7ºF) high 0.4ºC (32.7ºF) winds from the SW at 4.7 m/s (10.6 mph) gusting to 17.4 m/s (38.9 mph)pressure at 7.10 hPa'


# In[4]:


mars_url = "https://space-facts.com/mars/"
pandas_mars = pd.read_html(mars_url)
pandas_mars


# In[9]:


clean_mars = pandas_mars[0]
clean_mars.columns = ['Mars','Earth']
clean_mars.head()


# In[13]:


marshtml = clean_mars.to_html()
marshtml


# In[ ]:


hemisphere_url = [
    {"title": "Cerberus Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Valles Marineris Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
]


# In[5]:


get_ipython().system('jupyter nbconvert --to script mission_to_mars.ipynb')


# In[ ]:




