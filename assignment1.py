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
df.head()

# %%
# What is the most favourite pub?
from collections import Counter
df = pd.read_csv ('armenian_pubs_csv.csv')
occurences = Counter(df['Fav_Pub'])
most_used_word = max(occurences, key = occurences.get)
# %%
# What is the average age and income of the respondents?
df.mean(axis='index')
# %%