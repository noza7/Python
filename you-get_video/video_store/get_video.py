import sys
from you_get import common as yg

down_path = 'Movies'
url = 'https://www.iqiyi.com/v_19rrjc5nw8.html'
# url = 'http://www.le.com/ptv/vplay/1069136.html'
sys.argv = ['you-get', '-o', down_path, url]
yg.main()
