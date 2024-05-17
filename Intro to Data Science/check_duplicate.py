import pandas as pd

df = pd.read_csv(r"C:\python code\Intro to Data Science\laptop-prices-analysis\Data\amazon_temporary.csv",index_col=0)
df.drop(df.columns[[0]], axis=1, inplace=True)
