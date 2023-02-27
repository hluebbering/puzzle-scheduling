#!/usr/bin/env python
# coding: utf-8

# # Notebook 1. Data Analysis
# 
# **1. Preliminary Data Analysis**
# 
#     1.1 Importing libraries and dataset 
#     1.2 Preliminary Data Analysis
#     
#     
# **2. Data Cleaning** 
# 
#     2.1 Separating columns
#     2.2 Fixing Data inconsistencies
#     2.3 Dealing with Missing values
#     2.4 Dealing with Outliers
#  
# **3. Merging Data**

# ## 1. Preliminary Data Analysis

# ### 1.1 Importing Libraries and Dataset

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")


# **Data 1: member_hold_times_and_packs.tsv**
# * memberID - Unique identifiers for each person
# * holdtime - number of days the person had the pack
# * puzzlepack - name of the pack (may have more than 1 puzzle per pack)

# In[2]:


# loading first data about member hold times 
# dataset has 1.9 mb size on disk

member_holdtime_df = pd.read_csv('data/member_hold_times_and_packs_Feb16_2023.tsv', 
                                 sep='\t', header=None, names=["memberID", 'holdtime', 'puzzlepack'])
member_holdtime_df.shape


# In[3]:


member_holdtime_df.head()


# **Data 2: packs.tsv**
# * memberID - Unique identifiers for each person
# * holdtime - number of days the person had the pack
# * puzzlepack - name of the pack (may have more than 1 puzzle per pack)

# In[4]:


# loading second data about puzzle packs
# dataset has 98kb size on disk
col_names = ['pack_name', 'brand', 'piece_count', 'difficulty_rating']
packs_df = pd.read_csv('data/packs_Feb16_2023.tsv', sep='\t', header=None, names = col_names)

packs_df.shape


# In[5]:


packs_df.head()


# ### 1.2 Preliminary Data Analysis
# This is done to understand the data better so we can clean it accordingly. Here are some questions we are exploring - 
#    1. Does packname have a pattern?
#    2. What is the distribution for holdtimes?
#    3. Is there an evident relationship between difficulty rating and piece counts?

# > 1. Does packname have a pattern?

# In[6]:


## Does packname have a pattern?
pd.options.display.max_colwidth = 200
member_holdtime_df['puzzlepack'][0:5]


# **Comments**:
# - Observe the extra space at the end of "cats ". This shows it has this pack has only one puzzle.
# - other strings have the word "Puzzles" twice while 'Diana Zimens City Of Cats ' has it only once. 
# - Looks like the first word is a brand or something, then the word "puzzle" and the name of puzzle. For example -
#     * DaVici, **Puzzles** Full Moon Feast DaVici **Puzzles** World&#39;s Greatest Miracle 
#     * DaVici, **Puzzles** Flying Frigate DaVici **Puzzles** Hobby Horse
#     * Liberty, **Puzzles** Haeckel Hummingbirds Nautilus **Puzzles** Mother Adams
#     * DaVici, **Puzzles** Diana Zimens City Of Cats 
# 

# > 2. What is the distribution for holdtimes?
# 

# In[7]:


## What is the distribution for holdtimes?
fig, axs = plt.subplots(1, 2, figsize=(15, 5))
sns.histplot(data=member_holdtime_df, x=member_holdtime_df.loc[member_holdtime_df['holdtime'] < 150]['holdtime'], bins = 20,color="#ffa07a", alpha = 1.0, ax=axs[0])
axs[0].set_title("Holdtime up to 5 months")
sns.histplot(data=member_holdtime_df, x=member_holdtime_df.loc[member_holdtime_df['holdtime'] > 151]['holdtime'], bins = 20, color="#FB607F", alpha = 0.9, ax=axs[1])
axs[1].set_title("Holdtime over 5 months")
fig.tight_layout()
#plt.savefig("_static/images/hold_times_dist2.png", format="png", dpi=1200)
plt.show()


# **Comments:**
# Need to remove outliers in this case
# 
# 

# > 3. Is there an evident relationship between difficulty rating and piece counts?
# 
# - Separate columns into `piece_count_1`, `piece_count_2`, `difficulty_rating_1`, `difficulty_rating_2`

# In[8]:


## Is there an evident relationship between difficulty rating and piece counts?
# making two coulmns for piece count
packs_df['piece_count_1'] = packs_df['piece_count'].str.split(',', expand=True)[0]
packs_df['piece_count_2'] = packs_df['piece_count'].str.split(',', expand=True)[1]
# making two columns for difficulty
packs_df['difficulty_rating_1'] = packs_df['difficulty_rating'].str.split(',', expand=True)[0]
packs_df['difficulty_rating_2'] = packs_df['difficulty_rating'].str.split(',', expand=True)[1]


# In[9]:


# creating temporary dataframe with no missing values for analysis
packs_df_temp_1 = packs_df.dropna(axis=0, subset = ['piece_count_1', 'difficulty_rating_1'])
packs_df_temp_2 = packs_df.dropna(axis=0, subset = ['piece_count_2', 'difficulty_rating_2'])


# In[10]:


packs_df_temp_1.piece_count_1 = packs_df_temp_1.piece_count_1.astype('int')
packs_df_temp_2.piece_count_2 = packs_df_temp_2.piece_count_2.astype('int')


# In[11]:


packs_df.difficulty_rating.unique()


# In[12]:


# checking category-wise distribution of piece_count
plt.figure(figsize = [12,10], dpi=100)
color_dict = {'A-Easy':"g", 'Average':"b", 'Hard':"c", 'Really-Hard': "m"}

plt.subplot(2,1,1)
sns.boxplot(x = "piece_count_1", y= 'difficulty_rating_1', data=packs_df_temp_1, 
            palette = color_dict, order = ['A-Easy', 'Average', 'Hard', 'Really-Hard'])
plt.title("Puzzle one distribution")


plt.subplot(2,1,2)
sns.boxplot(x = "piece_count_2", y= 'difficulty_rating_2', data=packs_df_temp_2, 
            palette = color_dict, order = ['A-Easy', 'Average', 'Hard', 'Really-Hard'])
plt.title("Puzzle two distribution")
plt.legend(loc='lower right')
plt.show()


# **Comments:**
# 
# * "Easy" has the lowest median in both cases and "Hard" has the highest median.
# * Need to check this again after data cleaning (outlier removal) at a pack level.
# 

# ## 2. Data Cleaning

# ### 2.1 Separating columns
# 
# 
# Separate columns into 
# - `pack_name`, `brand_0`, `brand_1`, `piece_count_0`, `piece_count_1`, `difficulty_0`, `difficulty_1`

# In[13]:


# splitting brand name
packs_df['brand_2'] = packs_df['brand'].str.split(',', expand=True)[1]
packs_df['brand_1'] = packs_df['brand'].str.split(',', expand=True)[0]
# piececount and difficulty were split previously


# In[14]:


# adding number of puzzles feature
packs_df['num_puzzles'] = packs_df['pack_name'].map(lambda n: 1 if (n[-1] == ' ') else 2, na_action='ignore')


# In[15]:


# fixing datatype - convert piece_count values to integers
packs_df = packs_df.astype({'piece_count_1': 'int64', 'piece_count_2': 'int64'}, errors='ignore')


# In[16]:


# checking if we have any duplicate pack names
packs_df.drop_duplicates(['pack_name']).shape, packs_df.shape


# In[17]:


# # Packs with missing difficulty_rating and piece_count are present in members table?
# na_pack_name = packs_df[packs_df[['brand','piece_count', 'difficulty_rating']].isnull().any(axis=1)]
# len(set(na_pack_name['pack_name']).intersection(member_holdtime_df['puzzlepack']))

# -- this code is wrong, need to find a new function instead of .any

# Number of null values
packs_df.isnull().sum()


# In[18]:


# dropping the initial variables
packs_df.drop(['brand', 'piece_count', 'difficulty_rating'], axis=1, inplace=True)


# ### 2.2 Fixing Data inconsistencies

# In[19]:


# Some rows straight up have nothing, drop these as there is nothing to be done
packs_df.dropna(subset = ['difficulty_rating_1', 'difficulty_rating_2', 'piece_count_1', 'piece_count_2', 
                          'brand_1', 'brand_2'], how='all', inplace = True)


# In[20]:


# Puzzles with num = 1 but 2 piece_count values
packs_df[(packs_df.num_puzzles == 1) & (packs_df.brand_2.notna() | packs_df.piece_count_2.notna())].head()


# In[21]:


# Some 1 puzzle packs have a second number for pieces, this seems to be legit, updating to be 2 puzzle packs
packs_df.loc[((packs_df.num_puzzles == 1) & (packs_df.piece_count_2.notna())), 'num_puzzles'] = 2


# In[22]:


# Some 2 puzzle packs do not have piece count info for second puzzle. 
packs_df[(packs_df.piece_count_2.isna()) & (packs_df.num_puzzles == 2)].head()


# > For the packs you don't have any piece count data for, assume they are 2 puzzle packs, each with piece count equal to the global average piece count, OR if you can tell what brand it is, use the average for that brand (major brands are: Liberty, Artifact, Ecru, Wentworth, Nautilus, Stave)

# In[23]:


packs_df.piece_count_1 = packs_df.piece_count_1.astype('float').astype('Int64')
packs_df.piece_count_2 = packs_df.piece_count_2.astype('float').astype('Int64')
# what is the global average piececount?
packs_df['piece_count_1'].mean(),packs_df['piece_count_2'].mean()


# In[24]:


avg_pc2 = packs_df['piece_count_2'].mean()


# In[25]:


# making the piececount_2 same as piececount_1 IF num_puzzles ==2
packs_df.loc[((packs_df['piece_count_2'].isna() ) &(packs_df['num_puzzles'] ==2)), 'piece_count_2'] = int(avg_pc2)


# In[26]:


# making the brand_2 same as brand_1
packs_df.loc[(packs_df['brand_2'].isna()), 'brand_2'] = packs_df['brand_1']


# In[27]:


# packs with 1 puzzle but 2 brands? 


# ### 2.3 Dealing with Missing value

# In[28]:


member_holdtime_df.isnull().sum()


# In[29]:


member_holdtime_df.nunique()


# **Comments:**
# - No missing values in the data
# - We have information about 675 members and 910 unique puzzle packs

# In[30]:


packs_df.isnull().sum()


# In[31]:


packs_df.nunique()


# **Comments:Imputing missing values strategy**
# - Rows with missing difficulty_rating and piece_count are removed (none of these were seen in members data)
# - Brand: 
#     * if brand_2 and brand_1 has value - put same value (done in 2.2)
#     * for rest of them - replace missing with unknown
# - piece_count:
#     * Calculate average_piece_count at diffuclty level 
#     * for one puzzle: replace nan with average_piece_count
#     * for two puzzles: replace nan with average_piece_count twice

# In[32]:


packs_df[['brand_1', 'brand_2']] = packs_df[['brand_1', 'brand_2']].fillna('unknown')


# In[33]:


# puzzles which have no value for both piece_1 and piece_2 are dropped
packs_df.dropna(subset = ['piece_count_1', 'piece_count_2'], inplace=True, how='all')


# In[34]:


packs_df['piece_count_2'].fillna(0, inplace=True)
packs_df['difficulty_rating_2'].fillna('Average', inplace=True)


# ### 2.4 Dealing with Outliers

# In[35]:


member_holdtime_df = member_holdtime_df[(member_holdtime_df['holdtime'] >= 0.1) & 
                                        (member_holdtime_df['holdtime'] <= 150)]


# ## 3. Merging Data

# In[36]:


member_holdtime_df.puzzlepack.nunique(), packs_df.pack_name.nunique(), 


# In[37]:


df = member_holdtime_df.merge(packs_df, left_on='puzzlepack', right_on='pack_name', how='inner')
df.head(2)


# In[38]:


difficulty_mapping = {'A-Easy': 1, 'Average': 2, 'Hard': 3, 'Really-Hard': 4}

df['difficulty_rating_1'] = df['difficulty_rating_1'].map(lambda x: difficulty_mapping[x], na_action='ignore')
df['difficulty_rating_2'] = df['difficulty_rating_2'].map(lambda x: difficulty_mapping[x], na_action='ignore')


# In[39]:


df.isnull().sum()


# In[40]:


# masking puzzle names 
df.drop(['puzzlepack'], axis=1, inplace = True)


# In[41]:


df.to_csv('data/members_packs_cleaned.csv', index=False)

