# 2024/3/5 19:05
import random
import threading
import time

import video_id
import video_url
import download


def main():
    # 多线程
    fut_list = list()

    # 获取8页文本信息
    for i in range(8):
        # 获取每一页的文本信息
        info = video_id.get_video_id(i)

        # 从文本中提取video_id、title
        for id_title in video_id.parse(info):
            video_id_ = id_title[0]
            title = id_title[1]
            # 获取video_id_所对应的视频url
            video_url_ = video_url.get_video_url(video_id_)
            # # 下载视频
            # download.download_video(video_url_, title)
            # # 下载一个视频休眠1到2秒，避免服务器过载
            # time.sleep(random.uniform(1.0, 2.0))

            # 多线程
            t = threading.Thread(target=download.download_video, args=(video_url_, title))
            fut_list.append(t)

    print('开启多线程...')
    for t in fut_list:
        t.start()

    print('等待子线程执行...')
    for t in fut_list:
        t.join()


if __name__ == '__main__':
    now = time.time()
    main()
    print(f'耗时：{time.time() - now:.2f}s')
