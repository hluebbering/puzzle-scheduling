#!/usr/bin/env python
# coding: utf-8

# ## 1. Preliminary Data Analysis
# 
# ### 1.1 Importing Libraries and Dataset
# 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy



# 
# 
# ## Puzzles Data Cleaning
# 
# 
# > Part 1. Member Info Data Clean
# 
# **1. member_hold_times_and_packs.tsv**
# * `memberID` - Unique identifiers for each person
# * `holdtime` - number of days the person had the pack
# * `puzzlepack` - name of the pack (may have more than 1 puzzle per pack)

# In[2]:


# Import and preview members data
member_df = pd.read_csv("data/member_hold_times_and_packs.tsv", sep='\t', header=None, names=["member", 'hold_time', 'pack_name'])
member_df.head()


# In[3]:


# Number of null values
member_df[member_df['pack_name'].isna()]
member_df.isnull().sum()


# - No missing values in the data
# - We have information about 675 members and 910 unique puzzle packs

# #### Remove outliers
# 
# - Hold times $< 0.1$ are an artifact of their DB def wrong
# - Hold times $> 200$ days could be real but are probably noise

# In[4]:


print("Hold times < 0.1 |", len(member_df[member_df.hold_time < 0.1]))
print("Hold times > 200 |", len(member_df[member_df.hold_time > 200]))
print("Hold times Total |", len(member_df))


# In[5]:


member = member_df[(member_df.hold_time >= 0.1) & (member_df.hold_time <= 200)]
member.info()


# In[6]:


# Save data to csv file
member.to_csv("data/member_cleaned.csv", index = False)


# #### Thoughts:
# 
# - Without the dates the members got the packs, we can only rely on overall dist of user behavior
# - Signal such as seasonality and trends in user behavior are lost
# - We can't forcast "number of packs in $N$ days" with this info
# - From this info we can at best predict "expected hold time for user $X$ and pack $Y$"

# ----------------------------------------------------
# 
# ## Packs Data Cleaning
# 
# > Part 2. Initial Packs Data Clean
# 
# 
# **2. packs.tsv**
# * `pack_name` - name of the pack (may have more than 1 puzzle per pack)
# * `brand` - brand name of puzzle pack
# * `piece_count` - number of pieces in puzzle
# * `difficulty_rating` - difficulty rating for puzzle
# 
# 
# **Comment:**
# - Members data has 910 unique packs but packs dataframe has info about 909 packs
# - After combining all packs information, (splitting out a new row for packs with different brands, piece counts, and difficulty ratings) there are 1725 unique entries, 821 rows for brand are null, 259 rows for piece count are null, and 88 rows for difficulty rating are null
# - there are 909 unique packs, 9 unique pack names, and 4 unique types of difficulty ratings available
# - the mean piece count is about 359, with a standard deviation of 196, a min of 30, and a max of 1500
#     - the histogram plot for piece count looks slightly skewed
# - the most frequent brand that appears in the table is Artifact and the most frequent difficulty rating amongst the packs is average

# In[7]:


# Import and preview packs data
col_names = ['pack_name', 'brand_all', 'piece_count_all', 'difficulty_all']
packs_df = pd.read_csv("data/packs_Jan14_better.tsv", sep= "\t", header = None, names = col_names)
packs_df.head()


# In[8]:


# Number of null values
packs_df.isnull().sum()


# Separate columns into 
# - `pack_name`, `brand_0`, `brand_1`, `piece_count_0`, `piece_count_1`, `difficulty_0`, `difficulty_1`

# In[9]:


# Split brands
brands_split = packs_df['brand_all'].str.split(',', n=1, expand=True).rename(columns={0:'brand_0', 1:'brand_1'})

# Split pieces
piece_count_split = packs_df['piece_count_all'].str.split(',', n=1, expand=True).rename(columns={0:'piece_count_0', 1:'piece_count_1'})

# Split difficulty
diff_split = packs_df['difficulty_all'].str.split(',', n=1, expand=True).rename(columns={0:'diff_0', 1:'diff_1'})


# Add separated columns to dataframe

# In[10]:


# load data into a DataFrame object:
packs_split = packs_df.join([brands_split, piece_count_split, diff_split])

# Drop columns
packs_split = packs_split.drop(['brand_all', 'piece_count_all', 'difficulty_all'], axis=1)

# Get number of puzzles in pack
packs_split['num_puzzles'] = packs_df['pack_name'].map(lambda n: 1 if (n[-1] == ' ') else 2, na_action='ignore')
packs_split.head()


# In[11]:


# Save cleaned dataframe to csv file
packs_split[packs_split['pack_name'].duplicated(keep = False)]
packs_split.to_csv("data/packs_cleaned.csv")


# > Part 3. Remove NA Values

# In[12]:


# Find and count missing values
na_names = packs_split[packs_split['pack_name'].isna()]
na_brand_0 = packs_split[packs_split['brand_0'].isna()]
na_brand_1 = packs_split[packs_split['brand_1'].isna()]
na_piece_0 = packs_split[packs_split['piece_count_0'].isna()]
na_piece_1 = packs_split[packs_split['piece_count_1'].isna()]
na_diff_0 = packs_split[packs_split['diff_0'].isna()]
na_diff_1 = packs_split[packs_split['diff_1'].isna()]

print("NA pack name:", len(na_names), 
      "\nNA brand 0:", len(na_brand_0), "| NA brand 1:", len(na_brand_1),
      "\nNA piece count 0:", len(na_piece_0), "| NA piece count 1:", len(na_piece_1), 
      "\nNA difficulty:", len(na_diff_0), "| NA difficulty:", len(na_diff_1))


# In[13]:


# Convert piece_count values to integers
packs_split = packs_split.astype({'piece_count_0': 'int64', 'piece_count_1': 'int64'}, errors='ignore')


# In[14]:


# Drop rows that have no data across all columns
packs_filtered = packs_split.dropna(subset = ['brand_0', 'brand_1', 'piece_count_0', 'piece_count_1', 'diff_0', 'diff_1'], how='all')


# Some single puzzle packs have a 2 puzzle piece counts -- update to 2 puzzle packs
# 

# In[15]:


# Some 1 puzzle packs have a second number for pieces, this seems to be legit, updating to be 2 puzzle packs
packs_filtered.loc[((packs_filtered['num_puzzles'] == 1) & 
                    (packs_filtered['piece_count_1'].notna())), 'num_puzzles'] = 2


# In[16]:


# Could just drop the 2 puzzle rows that don't have full piece info?
packs_filtered_2 = packs_filtered[~(packs_filtered['num_puzzles'] == 2 & 
                                    packs_filtered['piece_count_1'].isna())]


# In[17]:


# packs_filtered_2.to_csv("data/packs_cleaned_dropna.csv")
packs_filtered_2.to_csv("data/packs_cleaned_dropna.csv",index = False)

