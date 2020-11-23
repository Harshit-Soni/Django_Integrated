#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests,re


# In[4]:


def getReviews(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    r = requests.get(url,headers=headers)
    content = r.content
    content = BeautifulSoup(content, 'html.parser')
    reviews = content.find_all('div', {"data-hook":"review-collapsed"})
    reviews_list = [review.get_text().strip('\n') for review in reviews]
    return (reviews_list, content.title.string)
    
# In[ ]:




