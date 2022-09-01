import pandas as pd
#import sys

df = pd.read_json('Lp.json')

df_clean = pd.DataFrame()

#for x in df.index:
#  if any(s in df.loc[x, "B-D"] for s in ('Audemars', 'Rolex', 'Patek')):   ## Several brands plotting
#    df_clean = pd.concat([df_clean, df.loc[x]], ignore_index=True, axis=1)

for x in df.index:
  if '5065' in df.loc[x, "B-D"]:                                          ## Single brand plotting
    df_clean = pd.concat([df_clean, df.loc[x]], ignore_index=True, axis=1)

df_clean = df_clean.transpose()



df_clean.plot.area()

print(df_clean)