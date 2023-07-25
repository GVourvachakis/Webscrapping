import requests
from bs4 import BeautifulSoup
import pprint
import time

def scrape_hacker_news(pages):
    base_url = 'https://news.ycombinator.com/news?p='
    all_links = []
    all_subtext = []

    for page in range(1, pages+1):
        url = base_url + str(page)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')

        links = soup.select('.titleline > a') 
        subtext = soup.select('.subtext')

        all_links.extend(links)
        all_subtext.extend(subtext)

        # Add a delay of 3 seconds between requests
        time.sleep(3)

    return all_links, all_subtext

if __name__ == "__main__":
    pages_to_scrape = 10
    links, subtext = scrape_hacker_news(pages_to_scrape)

    # Print the results using pprint (pretty print) for a cleaner output
    pprint.pprint(links)
    pprint.pprint(subtext)

