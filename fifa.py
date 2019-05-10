import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1500)
sns.set(style = "ticks")
%matplotlib inline

player_df = pd.read_csv("../Desktop/dataset/data.csv")

numcols = [
 'Overall',
 'Potential',
'Crossing',
'Finishing',  'ShortPassing',  'Dribbling','LongPassing', 'BallControl', 'Acceleration',
       'SprintSpeed', 'Agility',  'Stamina']
catcols = ['Name','Club','Nationality','Preferred Foot','Position']
# Subset the columns
player_df = player_df[numcols+ catcols]
info = player_df.loc[:, ['Name', 'Overall', 'Club','Nationality', 'Position']]
top_rated = (player_df['Overall'] >=90)
top_rated_striker = (player_df['Overall'] >= 80) & (player_df['Position'] == 'ST')


display(player_df.head(5))
display(info.head(5))
display(info[top_rated])
display(info[top_rated_striker])
