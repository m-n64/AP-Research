import csv
import article_stats
import os
data = article_stats.article_data

try:
    latest_year = int(os.listdir('./csv_tables')[-1].split('.')[0])
except IndexError:
    latest_year = 1961
    
for folder in data:
    if folder.year < latest_year:
        pass
    else:    
        with open(f'./csv_tables/{folder.year}.csv', 'w', encoding='utf-8') as csvFile:
            for file in folder.files:  
                file.get_data()
                    
                headers = list(file.fpages[0].to_dict().keys())
                writer = csv.DictWriter(csvFile, fieldnames=headers)
                writer.writeheader()
                writer.writerows([article.to_dict() for article in file.fpages])
                print('Data Entered')

                        



                
            
