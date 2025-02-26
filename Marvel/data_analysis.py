import pandas as pd
from collect_data import sample



def format_dataframe(df_list):

    master_df = pd.concat([pd.DataFrame(df) for df in df_list])

    master_df['On Sale Date'] = pd.to_datetime(master_df['On Sale Date'])

    master_df.sort_values('On Sale Date')

    return master_df


hero_dfs = [format_dataframe(hero.to_df()) for hero in sample]

for df in hero_dfs:
    
    print(df.head())


