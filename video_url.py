# 2024/3/5 19:10
import requests

import gene_useragent


def get_video_url(video_id: str):
    headers = {
        "Referer": f"https://www.pearvideo.com/{video_id}",
        "User-Agent": gene_useragent.get_ua(),
    }
    url = "https://www.pearvideo.com/videoStatus.jsp"
    cont_id = video_id.split('_')[1]
    params = {
        "contId": cont_id,
    }
    response = requests.get(url, headers=headers, params=params)

    # 提取srcUrl的值
    src_url = response.json()['videoInfo']['videos']['srcUrl']
    # print(src_url)
    # 提取日期
    date = src_url.split('/')[-2]
    # print(date)
    # 提取用“-”分割后得到的数组的第二个值
    hd_id = src_url.split('-')[1]
    # print(hd_id)
    # 拼接视频的url
    video_url = f'https://video.pearvideo.com/mp4/short/{date}/cont-{cont_id}-{hd_id}-hd.mp4'
    return video_url


if __name__ == '__main__':
    print(get_video_url('video_1792472'))
