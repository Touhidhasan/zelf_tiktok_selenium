import requests

# ttwid

cookies = {
    'tt_csrf_token': '',
    'ttwid': '1%7CDXPxlevDUNQAK0jUuxwYNrXOxYmi24IUFwk0d0hRTQw%7C1728100117%7C7fd7b217b85e68c0580aa0ace862882fe973ce3bf802b3457754ae45abad0ab7',
    'tt_chain_token': '',
    'ak_bmsc': '',
    'tiktok_webapp_theme_source': 'system',
    'tiktok_webapp_theme': 'light',
    'delay_guest_mode_vid': '3',
}

headers = {
    'accept': 'application/json, text/plain, */*',
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
    'x-pns-referrer': 'https://www.tiktok.com/search/video',
    'x-web-privacy-sdk-ver': '1.0.1',
}

params = {
    'locale': 'en',
    'appId': '1988',
    'theme': 'default',
    'tea': '1',
}

response = requests.get(
    'https://www.tiktok.com/api/v1/web-cookie-privacy/config',
    params=params,
    cookies=cookies,
    headers=headers,
)

print(response.status_code)
# print(response.text)
# print(response.cookies)
json_respone=response.json()
device_id=json_respone['body']['consent']['wid']
print(device_id)