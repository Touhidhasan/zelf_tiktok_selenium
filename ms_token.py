import requests
cookies = {
    'tt_csrf_token': '',
    'tt_chain_token': '',
    'ak_bmsc': '',
    'ttwid': '',
    'msToken': 'mboj_m6nKsn7sR6HE2jZq8MoX_SXeK2y4rr8zpV6YSUAZyrLtscCgOdrnr5MuoEK_K2Uu4i05yZ5z2szMRxCOQkDtPTXn1RXNIUJH-IUCt1h2xOw8FRcDWkvhoJR6GWqlb2S68SpqDA5qZbfRs1tYnJ7rw==',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Origin': 'https://www.tiktok.com',
    'Referer': 'https://www.tiktok.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
def get_token():
    data = '{"magic":538969122,"version":1,"dataType":8,"strData":"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","tspFromClient":1728105067857}'

    response = requests.post(
        'https://mssdk-sg.tiktok.com/web/report?msToken=mboj_m6nKsn7sR6HE2jZq8MoX_SXeK2y4rr8zpV6YSUAZyrLtscCgOdrnr5MuoEK_K2Uu4i05yZ5z2szMRxCOQkDtPTXn1RXNIUJH-IUCt1h2xOw8FRcDWkvhoJR6GWqlb2S68SpqDA5qZbfRs1tYnJ7rw==&X-Bogus=DFSzswVYqHn-K1-ltBf/kMSwXQ0C',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    try:
        token=response.cookies.get('msToken')
        print(token)
    except:
        token = None
    return token