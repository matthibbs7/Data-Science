# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 17:51:47 2021

Web Scraping Demo

@Matthew Hibbs
"""

#!pip install bs4
#!pip install requests

from bs4 import BeautifulSoup # For web scraping
import requests # Helps download webpage

# example
html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
soup = BeautifulSoup(html, 'html5lib')

print(soup.prettify())

# Tag object
tag_obj = soup.title
# Prints the <title>item</title> part of html
print("Tag object:", tag_obj)

# H3 obj
tag_obj = soup.h3


# Access Child of Tag tree Structure

tag_child = tag_obj.b

# Or Parent of tag
parent_tag = tag_child.parent

# Or go to next sibling
sibling_1 = tag_obj.next_sibling
sibling_2 = sibling_1.next_sibling

# Salary <p>
#sibling_2.next_sibling







