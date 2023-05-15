import pandas as pd

clothing_data = pd.read_csv('myntra_products_catalog.csv')
# insert into dataframes
df = pd.DataFrame(clothing_data)

df.head()
