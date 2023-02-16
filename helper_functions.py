import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import random
import time

def convert_day(day):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    m = 0
    d = 0
    while day > 0:
        d = day
        day -= month_days[m]
        m += 1
    return (m, d)

def get_claps(claps_str):
    if (claps_str is None) or (claps_str == '') or (claps_str.split is None):
        return 0
    split = claps_str.split('K')
    claps = float(split[0])
    claps = int(claps*1000) if len(split) == 2 else int(claps)
    return claps

#https://hackernoon.com/how-to-scrape-a-medium-publication-a-python-tutorial-for-beginners-o8u3t69
def get_article_text(story_url):
    
    story_page = requests.get(story_url)
    story_soup = BeautifulSoup(story_page.text, 'html.parser')

    sections = story_soup.find_all('section')
    story_paragraphs = []
    section_titles = []
    
    for section in sections:
        paragraphs = section.find_all('p')
        for paragraph in paragraphs:
            story_paragraphs.append(paragraph.text)

        subs = section.find_all('h1')
        for sub in subs:
            section_titles.append(sub.text)

    number_sections = len(section_titles)
    number_paragraphs = len(story_paragraphs)
    section_title_text = " ".join(section_titles)
    story_text = " ".join(story_paragraphs)
    
    return number_sections, number_paragraphs, section_titles, story_text

def rand_sleep():
    time.sleep(3 + random.gauss(0,1))
