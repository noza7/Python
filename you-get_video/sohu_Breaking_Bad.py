import re, sys
from bs4 import BeautifulSoup
from urllib import request, parse
from you_get import common as yg

# 《绝命毒师》视频查询地址
url = 'https://so.tv.sohu.com/mts?wd=%E7%BB%9D%E5%91%BD%E6%AF%92%E5%B8%88&box=1'
# https://tv.sohu.com/v/MjAxMzA4MTIvbjM4Mzk3NTg4My5zaHRtbA==.html
#       //tv.sohu.com/v/MjAxMjA3MjYvbjM0OTExMjk0Ny5zaHRtbA==.html
response = request.urlopen(url).read()
soup = BeautifulSoup(response, 'html.parser')
# 一定要转换soup为字符串类型
text = str(soup)
# 找到剧集所在季
pattern = '(.*?)绝命毒师第5季'
video_5s = re.findall(pattern, text)
video_urls = []
for url in video_5s:
    pattern = 'href="//tv.sohu.com/v/(.*?)==.html"'
    video_url = re.findall(pattern, url)
    if video_url:
        video_urls.append(video_url[0])
# 列表去重
video_urls = list(set(video_urls))
# print(video_urls)

# 获取真实视频地址列表
video_urls_ls = []
for video_url in video_urls:
    video_urls_ls.append('https://tv.sohu.com/v/{}==.html'.format(video_url))
print(video_urls_ls)
# 如果发生中断需要从断点提取
# for i in range(41, 43):
#     print(video_urls[i])
#     video_urls_ls.append('https://v.youku.com/v_show/id_{}'.format(video_urls[i]))

# 下载视频
down_path = 'e:/video_down/绝命毒师'
for url in video_urls_ls:
    sys.argv = ['you-get', '-o', down_path, url]
    yg.main()
