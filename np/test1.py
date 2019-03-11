import numpy as np
import pandas as pd

a = ['one', 'two', 'three']
b = [1, 2, 3]

english_column = pd.Series(a, name='english')
print(english_column)
number_column = pd.Series(b, name='number')
print(number_column)
predictions = pd.concat([english_column, number_column], axis=1)
print(predictions)
# save = pd.DataFrame({'english': a, 'number': b})
save = pd.DataFrame(predictions)
save.to_csv('b.csv', index=False, sep=' ')
