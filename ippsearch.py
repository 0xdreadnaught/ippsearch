#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import re

page=requests.get("https://www.youtube.com/channel/UCa6eh7gCkpPo5XXUDfygQQA/videos")
soup=BeautifulSoup(page.content, 'html5lib')

links=soup.find_all('a', class_="yt-uix-sessionlink yt-uix-tile-link spf-link yt-ui-ellipsis yt-ui-ellipsis-2")
for index in range(len(links)):
	url="https://youtube.com"+links[index]['href']
	print links[index]['title']+" ("+url+")"
        vidpage=requests.get(url)
        vidsoup=BeautifulSoup(vidpage.content, 'html5lib')
	description=vidsoup.find(id="eow-description")
	rawtext=description.text
	pattern = r'(\d{2}:\d{2} - )'
	replacement_string = r'\n\1'
	print re.sub(pattern, replacement_string, rawtext)
	print "\n\n"
