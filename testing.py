import requests #allows us to grab HTML files (most web pages are written in html)

from bs4 import BeautifulSoup #allows us to use that data we've gathered to do whatever we want to it, to scrape it.

import pprint #built-in module for aesthetic printing in terminal

# res = requests.get('https://news.ycombinator.com/news')

# print(res) -> <Response [200]>

#print(res.text) -> All the text information of this site in html

#Using BeautifulSoup we can convert the string into an (soup) object for futher manipulation 

# soup = BeautifulSoup(res.text, 'html.parser')

#print(type(soup)) -> <class 'bs4.BeautifulSoup'>

#print(soup.find_all('TAG')) -> gives in a string the text associated with the given tag

#print(soup.title) -> <title>Hacker News</title>

'''
print(soup.select('.score'))

Output structure:
    [<span class="score" id="score_36811554">117 points</span>, 
     <span class="score" id="score_36811018">98 points</span>,
     ...
    <span class="score" id="score_36803124">465 points</span>] 
'''

# links = soup.select('.titleline > a')

# subtext = soup.select('.subtext')

#print(votes[0])  -> <span class="score" id="score_36811554">130 points</span>

#print(votes[0].get('id'))  -> score_36811554

#Read the 2nd page of the website as well:
# res2 = requests.get('https://news.ycombinator.com/?p=2')

# soup2 = BeautifulSoup(res2.text, 'html.parser')

# links2 = soup2.select('.titleline > a')

# subtext2 = soup2.select('.subtext')

#Combine both pages:
# mega_links = links + links2
# mega_subtext = subtext + subtext2

#expand the web scraping to 10 pages
