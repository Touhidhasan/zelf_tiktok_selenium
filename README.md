# TikTok Scraper

I initially attempted to use the requests library, but due to TLS fingerprinting issues, I switched to undetected_chromedriver. In a production environment, we plan to use requests. We solved the CAPTCHA manually during development, but in production, we will implement a CAPTCHA solver.
## Overview

The TikTok Scraper is a Python-based tool that automates the process of scraping video data from TikTok based on specified keywords. This scraper uses Selenium and `undetected_chromedriver` to bypass potential bot detection mechanisms and gather video information, including URLs, captions, author usernames, and follower counts.

## Features

- Scrapes TikTok videos based on specified keywords.
- Gathers video metadata: 
  - Video URL
  - Video Caption
  - Author Username
  - Follower Count
  - Following Count
  - Like Count
- Outputs data to a CSV file for easy access and analysis.

