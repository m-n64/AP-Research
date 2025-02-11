import csv
import article_stats
import os
data = article_stats.article_data

try:
    latest_year = int(os.listdir('./csv_tables')[-1].split('.')[0])
except IndexError:
    latest_year = 1961
    
with open(f'./data.csv', 'w', encoding='utf-8') as csvFile:
    
    has_header = False
    for folder in data:
        for file in folder.files:  
            file.get_data()
            headers = list(file.fpages[0].to_dict().keys())
            writer = csv.DictWriter(csvFile, fieldnames=headers)
            
            if has_header == False:
                writer.writeheader()
                has_header = True
            
            writer.writerows([article.to_dict() for article in file.fpages])
            print('Data Entered')

                        

            
