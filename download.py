import datetime
import os.path

import requests


def download_video(video_url, title):
    fail = open('fail.txt', 'a', encoding='utf-8')
    try:
        if not os.path.exists('./video'):
            os.mkdir('./video')
        response = requests.get(video_url, stream=True)
        with open(f'./video/{title}.mp4', 'wb') as fw:
            for chunk in response.iter_content(chunk_size=1024):
                fw.write(chunk)
        print(f'“{title}” 下载成功...')
        response.close()
    except Exception as e:
        print(f'“{title}” 下载失败...', e)
        fail.write(f'({datetime.datetime.now()} {video_url},{title})\n')
    fail.close()


if __name__ == '__main__':
    download_video('https://video.pearvideo.com/mp4/short/20240305/cont-1792472-71105962-hd.mp4', '周除')
