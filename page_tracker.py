import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

insta_text = 'The link you followed may be broken, or the page may have been removed.'

tiktok_text = 'Video currently unavailable'
tiktok_good_text = 'Verify to continue:'

facebook_text = 'You must log in to continue.'
another_facebook_text = 'The link you followed may be broken, or the page may have been removed.'
and_another_one = 'The link may be broken or the video may have been removed. You can explore more videos or try logging in to facebook.com and then visiting the link again.'

twitter_text = 'Something went wrong. Try reloading.'
another_twitter_text = 'Hmm...this page doesn’t exist. Try searching for something else.'

linkedin_text = 'Page not found'
another_linkedin_text = 'Make the most of your professional life'

youtube_text = 'This video is no longer available'
another_youtube_text = 'This video isn\'t available any more'

def check_page(url):
    options = Options()
    options.headless = True  # Set to True if you don't want the browser to open

    driver = webdriver.Chrome(options=options)  # Make sure to provide the correct path to your chromedriver executable
    driver.get(url)

    # Wait for the page to load (adjust the time.sleep value as needed)
    time.sleep(5)

    page_source = driver.page_source

    #print(page_source)

    if 'instagram' in url:
        if insta_text in page_source:
            print("(+) this instagram page is blocked!")
        else:
            print("(-) this instagram page is still up!")
    if 'tiktok' in url:
        if tiktok_good_text in page_source:
            print("(-) this tiktok page is still up!")
        else:
            print("(+) this tiktok page is blocked!")
    if 'facebook' in url or 'fb' in url:
        if facebook_text in page_source or another_facebook_text in page_source or and_another_one in page_source:
            print("(+) this facebook page is blocked!")
        else:
            print("(-) this facebook page is still up!")
    if 'twitter' in url or 'x.com' in url:
        if twitter_text in page_source or another_twitter_text in page_source:
            print("(+) this twitter page is blocked!")
        else:
            print("(-) this twitter page is still up!")
    if 'linkedin' in url:
        if linkedin_text in page_source or another_linkedin_text in page_source:
            print("(+) this linkedin page is blocked!")
        else:
            print("(-) this linkedin page is still up!")
    if 'youtube' in url or 'youtu.be':
        if youtube_text in page_source or another_youtube_text in page_source:
            print("(+) this youtube page is blocked!")
        else:
            print("(-) this youtube page is still up!")
    driver.quit()

def main():
    if len(sys.argv) != 2:
        print("(+) usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    check_page(url)


if __name__ == "__main__":
    main()
