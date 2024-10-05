import requests
import json
import re
def FollowerFollowingLikes(user="i.am.brazil.suppo5"):
    cookies = {
        'tt_csrf_token': '',
        'tt_chain_token': '',
        'ak_bmsc': '',
        'tiktok_webapp_theme_source': 'system',
        'tiktok_webapp_theme': 'light',
        'delay_guest_mode_vid': '3',
        's_v_web_id': 'verify_m1vrcf7a_FkAFzppH_qsnO_41JC_BCyP_C2SGP20Sj7ky',
        'perf_feed_cache': '',
        'odin_tt': '',
        'bm_sv': '',
        'ttwid': '',
        'msToken': '',
        'passport_csrf_token': '',
        'passport_csrf_token_default': '',
        'msToken': '',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://www.tiktok.com/search/video?q=beautiful%20destinations',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    response = requests.get(f'https://www.tiktok.com/@{user}', cookies=cookies, headers=headers)

    print(response.status_code)


    data_string=response.text
    # print(data_string)


    # Use regular expression to search for followerCount
    match = re.search(r'"followerCount":(\d+)', data_string)
    match2 = re.search(r'"followingCount":(\d+)', data_string)
    match3 = re.search(r'"heart":(\d+)', data_string)

    # Check if a match was found and extract the followerCount
    if match:
        follower_count = int(match.group(1))
        print(f"Follower Count: {follower_count}")
    else:
        print("followerCount not found")
        follower_count=""

    if match2:
        following_count = int(match2.group(1))
        print(f"Following Count: {following_count}")
    else:
        print("followerCount not found")
        following_count=""

    if match3:
        like_count = int(match3.group(1))
        print(f"Like Count: {like_count}")
    else:
        print("followerCount not found")
        like_count=""

    # follower =
    # following =
    # like =


    return follower_count,following_count,like_count
# FollowerFollowingLikes()