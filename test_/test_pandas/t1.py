import pandas as pd

url = 'http://www.w3school.com.cn/html/html_tables.asp'
df = pd.read_html(io=url)
# df=pd.DataFrame(df)
print(df)
