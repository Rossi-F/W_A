import pandas as pd

df_lp = pd.read_json('Lp.json')
df_phill = pd.read_json('Phill.json')

df = pd.concat([df_phill, df_lp], ignore_index=True)

df_clean = pd.DataFrame()

#for x in df.index:
#  if any(s in df.loc[x, "B-D"] for s in ('Audemars', 'Rolex', 'Patek')):   ## Several brands plotting
#    df_clean = pd.concat([df_clean, df.loc[x]], ignore_index=True, axis=1)

for x in df.index:
  if 'Rolex' in str(df.loc[x, "B-D"]):                                          ## Single brand plotting
    df_clean = pd.concat([df_clean, df.loc[x]], ignore_index=True, axis=1)

df_clean = df_clean.transpose()

df_clean.plot()

print(df_clean)