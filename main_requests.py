import requests
import json
import urllib.parse

class TiktokScraper:
    def __init__(self):
        pass
    def keyword_scraper(self,keyword="beautiful destinations"):
        # Note: ttwid, device_id, msToken, and X - Bogus
        # are
        # required
        # for scraping using the requests module.I have successfully obtained ttwid, device_id, and msToken through individual APIs,
        # but I am unable to retrieve the X-Bogus value.For pagination, we need to increase the offset in increments of 12 (e.g., 0, 12, 24, etc.).
        # For offset=0, we are receiving 12 results using this method.

        # keyword .
        # odinId ?   same2
        # web_search_code ? same2
        # msToken ? samenot2
        # X - Bogus x   samenot2
        # offset pagination

        keyword_url = urllib.parse.quote(keyword)
        print(keyword_url)
        cookies = {
            'tt_csrf_token': '',
            'tt_chain_token': '',
            'ak_bmsc': '',
            'tiktok_webapp_theme_source': 'system',
            'tiktok_webapp_theme': 'light',
            'delay_guest_mode_vid': '3',
            'ttwid': '1%7CDXPxlevDUNQAK0jUuxwYNrXOxYmi24IUFwk0d0hRTQw%7C1728104893%7Cc5287b14c0bac67a7fa031a405ee79c114ce7800407a58f7d2a0b7de0fcb3953',
            's_v_web_id': '',
            'perf_feed_cache': '',
            'msToken': '',
            'msToken': '',
        }

        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'priority': 'u=1, i',
            'referer': 'https://www.tiktok.com/search/video?q=beautiful%20destinations',
            'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }



        response = requests.get(
            f'https://www.tiktok.com/api/search/item/full/?WebIdLastTime=1728100117&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F129.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&count=20&data_collection_enabled=false&device_id=7422133448406124040&device_platform=web_pc&focus_state=true&from_page=search&history_len=2&is_fullscreen=false&is_page_visible=true&keyword={keyword_url}&odinId=7422133390877541394&offset=0&os=windows&priority_region=&referer=&region=BD&screen_height=720&screen_width=1280&tz_name=Asia%2FDhaka&user_is_login=false&web_search_code=%7B%22tiktok%22%3A%7B%22client_params_x%22%3A%7B%22search_engine%22%3A%7B%22ies_mt_user_live_video_card_use_libra%22%3A1%2C%22mt_search_general_user_live_card%22%3A1%7D%7D%2C%22search_server%22%3A%7B%7D%7D%7D&webcast_language=en&msToken=2O3kzpxw1DsWfaRmFHO81ix-8D7Fecmm6wEpAOQg31GDAs7OuFi6t7M0jKTHL0ovMRzGn1SJfIPdtgI2qCBkXM2X5qPHwATzZkRydoFzUWI6fQkvHJOVDqEAlgxTpCKBIfSTnZYScx_be-puTO_MuQsz&X-Bogus=DFSzswVYLl2ANH-ltBvrvFSwXQ/m',
            cookies=cookies,
            headers=headers,
        )
        print(response.cookies)
        print(response.status_code)
        # print(response.text)

        json_response=response.json()
        # print(json_response)

        item_list=json_response['item_list']
        print(len(item_list))

        for item in item_list:
            post_id=item['id']
            # print(post_id)

            video_id=item['video']['id']
            print(video_id)

            author_unique_id=item['author']['uniqueId']
            print(author_unique_id)

            video_url=f"https://www.tiktok.com/@{author_unique_id}/video/{video_id}"
            print(video_url)

            video_caption=item['desc']
            print(video_caption)
            author_username=author_unique_id

            # author info
            username=author_unique_id
            follower_count=item['authorStats']['followerCount']
            print(follower_count)
            following_count=item['authorStats']['followingCount']
            print(following_count)
            like_count=item['authorStats']['heartCount']
            print(like_count)



if __name__ == '__main__':
    tiktok_scraper=TiktokScraper()

    tiktok_scraper.keyword_scraper()