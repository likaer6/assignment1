#%%
import pandas as pd
# %%
import numpy as np
#%%
df = pd.read_csv ('armenian_pubs_csv.csv')
# %%
df.shape 
# %%
df
# %%
df.info()
# %%
df.columns
# %%
# What is the most favourite pub?
from collections import Counter
df = pd.read_csv ('armenian_pubs_csv.csv')
occurences = Counter(df['Fav_Pub'])
most_used_word = max(occurences, key = occurences.get)
# %%
# What is the favorite pub among female and male visitors?
df_2 = pd.pivot_table(df, index = ["Gender ", "Fav_Pub"], aggfunc='size').sort_values(ascending=False)
df_2.to_csv("fav_pubs_by_gender.csv")
# %%
# What is the average age and income of the respondents?
df.mean(axis='index')
# %%
# What are most people willing to spend at the pub?
df["WTS"].value_counts()
# %%
# What is age that was given most of the times?
pd.pivot_table(df, index = ["Age "], aggfunc='size').sort_values(ascending=False)
# %%
df.describe()
# %%