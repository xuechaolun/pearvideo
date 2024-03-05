# 2024/3/5 19:10
import re

import requests

import gene_useragent


def get_video_id(page):
    headers = {
        "Referer": "https://www.pearvideo.com/popular",
        "User-Agent": gene_useragent.get_ua(),
    }
    url = "https://www.pearvideo.com/popular_loading.jsp"
    params = {
        "reqType": "41",
        "categoryId": "",
        "start": str(page*10),
        "sort": str(page*10),
    }
    response = requests.get(url, headers=headers, params=params)
    return response.text


def parse(data):
    video_id_list = re.findall('<a href="(.*?)" class="popularembd actplay">', data)
    title_list = re.findall('<h2 class="popularem-title">(.*?)</h2>', data)
    for video_id, title in zip(video_id_list, title_list):
        yield video_id, title


if __name__ == '__main__':
    data_ = get_video_id(0)
    for i in parse(data_):
        print(i)
