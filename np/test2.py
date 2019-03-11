import pandas as pd

excel_path = '新订单秦皇岛本.xlsx'
df = pd.read_excel(excel_path, sheet_name='青龙')
print(df)

