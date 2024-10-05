import requests
import re
import time
import urllib.parse
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import get_follower_following_likes
import csv

class TiktokScraper:
    def __init__(self):
        self.driver = uc.Chrome()

    def scrape_keywords(self, keyword):
        url_slug = urllib.parse.quote(keyword)
        self.driver.get(f"https://www.tiktok.com")
        self.driver.get(f"https://www.tiktok.com/search/video?q={url_slug}")
        time.sleep(3)
        input("Solve the captcha and press enter..")

        try:
            captcha_element = self.driver.find_element(By.XPATH, '//div[@class="captcha_verify_container CaptchaWrapper-u1rqd2-0 gmpebW"]')
            if captcha_element:
                input("Solve the captcha and press enter..")
        except:
            pass

        # Create or open the CSV file for writing
        with open('tiktok_videos.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Write the header only once, if the file is empty
            file.seek(0, 2)  # Move the cursor to the end of the file
            if file.tell() == 0:  # Check if the file is empty
                writer.writerow(['Video URL', 'Video Caption', 'Author Username', 'Follower Count', 'Following Count', 'Like Count'])

            video_count = 0
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            while True:
                video_list = self.driver.find_elements(By.XPATH, '//div[@data-e2e="search_video-item-list"]/div')
                print("Total videos:", len(video_list))
                time.sleep(5)

                for index, video in enumerate(video_list):
                    print(video_count)
                    try:
                        video_url = video_list[video_count].find_element(By.XPATH, './/div[@data-e2e="search_video-item"]//a').get_attribute('href')
                        print(video_url)
                    except:
                        video_url = None

                    try:
                        video_caption = video_list[video_count].find_element(By.XPATH, './/h1/span').text
                        print(video_caption)
                    except:
                        video_caption = None

                    try:
                        author_username = video_list[video_count].find_element(By.XPATH, './/p[@data-e2e="search-card-user-unique-id"]').text
                        print(author_username)
                    except:
                        author_username = None

                    pattern = r'https://www\.tiktok\.com/@([^/]+)/video/(\d+)'
                    match = re.search(pattern, video_url)
                    if match:
                        username = match.group(1)
                        print(f"Username: @{username}")
                    else:
                        print("No match found.")
                        username = None

                    if username:
                        follower_count, following_count, like_count = get_follower_following_likes.FollowerFollowingLikes(username)
                    else:
                        follower_count = following_count = like_count = None

                    print(follower_count, following_count, like_count)

                    # Write the scraped data to the CSV file
                    writer.writerow([video_url, video_caption, author_username, follower_count, following_count, like_count])

                    # Scroll down the page
                    self.driver.execute_script("window.scrollBy(0, 5000);")

                    video_count += 1

                time.sleep(20)

if __name__ == '__main__':
    tiktok_scraper = TiktokScraper()
    tiktok_scraper.scrape_keywords("beautiful destinations")
