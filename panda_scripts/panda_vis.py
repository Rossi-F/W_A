import pandas as pd

df = pd.read_json('LoupeThis.json')

df_clean = pd.DataFrame()

for x in df.index:
  if any(s in df.loc[x, "Brand/Description/Price"] for s in ('Rolex', 'Patek', 'Audemars')):
    df_clean = pd.concat([df_clean, df.loc[x]], ignore_index=True, axis=1)

df_clean = df_clean.transpose()

df_clean.plot.area()