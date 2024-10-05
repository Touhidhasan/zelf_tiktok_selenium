import csv
import requests

# URL to post data to
url = 'http://192.168.243.59:3000/api/video-data/'

# Open and read the CSV file
with open('tiktok_videos3.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    batch = []
    batch_size = 100  # Number of rows to send in each batch

    for row in reader:
        # Add each row to the batch
        if row['content']:
            myobj = {
                'video_url': row['url'],
                'video_caption': row['content'],
                'Query': row['Keyword'],
                'video_publisher': row['user']
            }
            batch.append(myobj)

        # Once the batch is full, post the data
        if len(batch) == batch_size:
            x = requests.post(url, json=batch)
            print(f"Batch response: {x.text}")
            batch.clear()  # Clear the batch after sending

    # Send any remaining data if it's less than 100
    if batch:
        x = requests.post(url, json=batch)
        print(f"Final batch response: {x.text}")
