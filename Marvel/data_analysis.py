import pandas as pd
from collect_data import sample
import os


def format_dataframe(df_list):

    master_df = pd.concat([pd.DataFrame(df) for df in df_list])

    master_df['On Sale Date'] = pd.to_datetime(master_df['On Sale Date'], utc=True)

    master_df = master_df.sort_values('On Sale Date')

    return master_df





if __name__ == '__main__':


    try: os.mkdir(f'./Marvel/dataframes')
    except FileExistsError: pass


    for hero in sample:
        
        for df in hero.to_df():
            print(print(pd.DataFrame(df)))

        hero_df = format_dataframe(hero.to_df())
        print(f'Completed {hero}')

        print(hero_df.head())

        hero_df.to_csv(f'./Marvel/dataframes/{hero}.csv', encoding='utf-8', index=False, header=True)



