import requests #allows us to grab HTML files (most web pages are written in html)

from bs4 import BeautifulSoup #allows us to use that data we've gathered to do whatever we want to it, to scrape it.

import pprint #built-in module for aesthetic printing in terminal

import time

import threading

import sys

import readchar


from web_scraping_pages import scrape_hacker_news


def sort_stories_by_votes(hn_list):
    return sorted(hn_list, key = lambda k:k['votes'], reverse = True)
    
def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        #print(vote) -> ex: [<span class="score" id="score_36807028">284 points</span>]
        if len(vote): #in case a story has non-zero votes
            points = int(vote[0].getText().replace(' points',''))
            #print(points)
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


def loading_animation(done_flag):
    # Customize your loading animation here
    animation = "|/-\\"
    i = 0
    while not done_flag.is_set():  # Keep running until the done_flag is set
        time.sleep(0.2)  # Adjust the animation speed
        print("Fetching data " + animation[i], end="\r")
        i = (i + 1) % len(animation)

def wait_for_exit():
    global exit_program_flag
    print("\nPress 'q' to prematurely terminate the program.\n")
    while not exit_program_flag:
        char = readchar.readchar()
        if char.lower() == 'q':
            exit_program_flag = True
            # Signal all other threads to terminate
            loading_done.set()

if __name__ == "__main__":
    exit_program_flag = False

    while True:
        try:
            page = int(input('how many pages in hacker news do you want to scrape?\n'))
        except ValueError:
            print('add a number please\n')
        else:
            break

   # Record the start time
    start_time = time.time()

    # Start the waiting for exit in the background using a separate thread
    exit_thread = threading.Thread(target=wait_for_exit)
    exit_thread.start()

    # Create a shared flag to signal the loading animation to stop
    loading_done = threading.Event()

    # Start the loading animation in the background using a separate thread
    loading_thread = threading.Thread(target=loading_animation, args=(loading_done,))
    loading_thread.start()

    # Perform the scraping
    mega_links, mega_subtext = scrape_hacker_news(page)

    # Set the loading_done flag to signal the loading animation to stop
    loading_done.set()

    # Wait for the loading animation thread to complete
    loading_thread.join()

    # Check if the exit_program_flag is set
    if exit_program_flag:
        sys.exit("\n\t\t\tProgram terminated by user.")  # Exit without displaying scraped data

    # Display the scraped data
    pprint.pprint(create_custom_hn(mega_links, mega_subtext))

    # Calculate the elapsed time and display it
    elapsed_time = time.time() - start_time
    print(f"\n\t\t\tScraping completed in {elapsed_time:.2f} seconds.")

    # Explicitly exit the program after displaying the scraped data and time taken
    sys.exit("\n\t\t\tScraped data displayed. Press 'q' to exit the program.\n")
