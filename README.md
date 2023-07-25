# Web Scraping Program Description:

The provided codes combine to form a web scraping program that scrapes news articles from Hacker News and displays the articles with a vote count of 100 or more. It consists of two components: One is the main Python script that is run from the terminal, included in 'web_scraper.py', and the other is a module ('web_scraping_pages.py') that performs the actual web scraping.

# Functionalities:

    The scrape_hacker_news function in the module performs web scraping on Hacker News pages. It takes the number of pages to scrape as input and returns two lists, all_links, and all_subtext. Each list contains elements representing the links and subtext (including vote count) of the articles on the corresponding pages.

    The create_custom_hn function in the main script filters the scraped data and selects articles with a vote count greater than 99. It returns a sorted list of dictionaries containing the title, link, and vote count of these articles.

    The sort_stories_by_votes function is a helper function that sorts the list of articles by vote count in descending order, allowing the articles to be displayed in order of popularity.

    The loading_animation function is used to display a loading animation in the terminal while the web scraping process is ongoing. It is run as a background thread to provide a visual indication that the program is working.

    The wait_for_exit function allows the user to prematurely terminate the program by pressing the 'q' key. It runs as a background thread to continuously check for user input.

    The main part of the script sets up the program by taking input from the user for the number of pages to scrape and initiates the loading animation and exit program threads. It then calls the scrape_hacker_news function to perform the actual web scraping. The results are then filtered and displayed using create_custom_hn, and the elapsed time is calculated and shown.

# Good Practices Included:

    Delay Between Requests: In the web scraping module, there is a delay of 3 seconds (time.sleep(3)) between consecutive requests to the website. This is done to be more considerate to the website's server and prevent potential issues like overloading their server with too many requests in a short period. Adding delays between requests is a good practice in web scraping to avoid getting blocked by the server or causing undue strain on it.

    Multithreading for User Experience: The program uses threading to display a loading animation and to allow the user to terminate the program prematurely. By running these tasks in separate threads, the main thread can continue with the web scraping process, and the user gets real-time feedback on the program's progress. This enhances the user experience and makes the program more interactive and user-friendly.

    Clear User Instructions: The program provides clear instructions to the user on how to terminate the program prematurely. It displays a message indicating that the user can press 'q' to exit, making the termination process straightforward and understandable.

    Aesthetic Printing with pprint: The pprint module is used for printing the scraped data in a more organized and aesthetically pleasing manner. This ensures that the data is easy to read and comprehend for the user.

    Error Handling: The program includes error handling for user input by using a try-except block to catch and handle ValueError if the user provides invalid input (e.g., entering a non-numeric value for the number of pages to scrape).

    Readability and Modularity: The code is organized into separate functions and modules, making it modular and easier to maintain. Each function has a specific purpose, making the code more readable and understandable.

Overall, the web scraping program demonstrates good practices in terms of user experience, website consideration, error handling, and code organization, making it a reliable and considerate web scraping tool.

