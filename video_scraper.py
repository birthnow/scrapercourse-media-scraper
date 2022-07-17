import requests
import os
import glob

#1.下載m3u8檔案
reponse = requests.get('https://edgecast-cf-prod.yahoo.net/cp-video-transcode/production/a090d67d-1beb-30d5-aead-fedb4f652472/2022-07-15/07-46-49/360c6c01-27bd-53d8-8ea4-07742ff56927/stream_340x192x221_v2.m3u8')

if not os.path.exists('video'):
    os.mkdir('video')

with open('video\\trailer.m3u8', 'wb') as file:
    file.write(reponse.content)


#2.下載ts檔案
ts_url_list = []
with open('video\\trailer.m3u8', 'r', encoding='utf-8') as file:
    contents = file.readlines()

    base_url = 'https://edgecast-cf-prod.yahoo.net/cp-video-transcode/production/a090d67d-1beb-30d5-aead-fedb4f652472/2022-07-15/07-46-49/360c6c01-27bd-53d8-8ea4-07742ff56927/'

    for content in contents:
        if content.endswith('ts\n'):
            ts_url = base_url + content.replace('\n', '')
            ts_url_list.append(ts_url)

for index, url in enumerate(ts_url_list):
    ts_response = requests.get(url)

    with open(f'video\\{index+1}.ts', 'wb') as file:
        file.write(ts_response.content)


#3.合併ts檔案
ts_files = glob.glob('video\\*.ts')

with open('video\\trailer.mp4', 'wb') as file:
    for ts_file in ts_files:
        file.write(open(ts_file, 'rb').read())