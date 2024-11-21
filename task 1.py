#!/usr/bin/env python
# coding: utf-8

# In[45]:


pip install beautifulsoup4 requests


# In[46]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[47]:


base_url = "https://www.airlinequality.com/airline-reviews/british-airways"
pages = 10
page_size = 100

reviews = []

# for i in range(1, pages + 1):
for i in range(1, pages + 1):

    print(f"Scraping page {i}")

    # Create URL to collect links from paginated data
    url = f"{base_url}/page/{i}/?sortby=post_date%3ADesc&pagesize={page_size}"

    # Collect HTML data from this page
    response = requests.get(url)

    # Parse content
    content = response.content
    parsed_content = BeautifulSoup(content, 'html.parser')
    for para in parsed_content.find_all("div", {"class": "text_content"}):
        reviews.append(para.get_text())
    
    print(f"   ---> {len(reviews)} total reviews")


# In[48]:


df = pd.DataFrame()
df["reviews"] = reviews
df.head()


# In[49]:


df.to_csv("data.csv")

