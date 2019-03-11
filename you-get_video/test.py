import re, sys
from bs4 import BeautifulSoup
from urllib import request, parse
from you_get import common as yg

down_path = 'e:/video_down/绝命毒师'
# url_1 = 'https://tv.sohu.com/v/MjAxMjA5MjgvbjM1NDEyNjQ4MS5zaHRtbA==.html'
# url_2 = 'https://tv.sohu.com/v/MjAxMzA4MTIvbjM4Mzk3NTg4My5zaHRtbA==.html'
# url_3 = 'https://tv.sohu.com/v/MjAxMzA4MjgvbjM1NDEyNjQ4MS5zaHRtbA==.html'
# url = 'https://www.iqiyi.com/v_19rrlhjlvc.html#vfrm=2-4-0-1'
url = 'http://v.youku.com/v_show/id_XMzY3OTQ0Nzk5Mg==.html?spm=a2h0j.11185381.listitem_page1.5!3~A&&s=7c1ecdcd435c11e6bdbb'
sys.argv = ['you-get', '-o', down_path, url]
yg.main()
