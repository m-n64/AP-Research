import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import json
import os


filter = {
    'The Soviet Union': [
        'UNION OF SOVIET SOCIALIST REPUBLICS',        
        'UNION OF SOVIET SOCIALISTS REPUBLICS',        
        'UNION OF SOVIET SOCIALIST REPUBLIC',

        'USSR',
        'USSR AND EAST EUROPEAN COMMUNIST NATIONS',
        'COMMUNISM',

        'BIG POWERS (FRANCE, GB, USSR AND US) MUTUAL RELATIONS AND COLD WAR',

    ],

    'The Space Race': [
        'AERONAUTICS AND SPACE ADMINISTRATION, NATIONAL',
        'SPACE AND UPPER ATMOSPHERE',
        'SPACE',
        
        'US SPACE PROGRAM (GENERAL)',
        'US SPACE PROGRAM (GEN)',
        'USSR SPACE PROGRAM (GENERAL)',

        'ASTRONAUTICS',
        'AERONAUTICS'


        

    ],

    'Radiation and Atomic Science': [
        'RADIATION AND RADIOACTIVITY',
        'RADIATION, EFFECTS AND HAZARDS OF',
        'Radiation',
        'RADIATION HAZARDS AND PROTECTION',
        'EFFECTS AND HAZARDS OF RADIATION',

        'ATOMIC ENERGY AND WEAPONS',
        'ATOMIC ENERGY',

        'ARMAMENT',
        'ARMAMENT, DEFENSE AND MILITARY FORCES',
        'ARMAMENT, DEFENCE AND MILITARY FORCES',
        'ARMAMENT, DEFENSE AND MIL FORCES',
        'US ARMAMENT, DEFENSE AND MIL FORCES',
        'UNITED STATES ARMAMENT AND DEFENSE',

        'NUCLEAR WEAPONS',
        'NUCLEAR RESEARCH',

    ],

    'Civil Rights': [
        'CIVIL RIGHTS MOVEMENT',
        'NEGROES',
        'NEGROS',

        'COLORED PEOPLE, NATIONAL ASSN',
        'COLORED PEOPLE, NATIONAL ASSN FOR THE ADVANCEMENT OF',
        
        'Malcolm X',
        'King, Martin Luther Jr',
        'KING, MARTIN LUTHER JR.'

    ],

    'Student Activism and Counterculture': [
        'STUDENT ACTIVITIES AND CONDUCT',
        'PEACE UNION, STUDENT',
        'Colleges and Universities',
        'DEMOCRATIC SOCIETY, STUDENTS FOR A',
        'STUDENT NONVIOLENT COORDINATING COMMITTEE',
        'AMERICANS FOR FREEDOM, YOUNG'
    ],

    'Vietnam': [
        'Vietnam',
        'DRAFT, RECRUITMENT AND MOBILIZATION',
        'DRAFT AND MOBILIZATION OF TROOPS',
        'DRAFT AND RECRUITMENT, MILITARY'
    ],

}

    
    





master = pd.read_csv('./NYT/dataframes/master.csv')


# first check the keywords, then check the headline, then check the abstract

def check_occurences(terms):
    
    wordcount = {}
            
    for index, row in master.iterrows():

        try:
            keywords = row['keywords'].split('||')
        except AttributeError:
            pass

        date = datetime.strptime(row['date'], f'%Y-%m-%d').strftime(f'%m/%Y')

        if date not in wordcount: wordcount[date] = 0

        for t in terms:
            if t in keywords:
                wordcount[date] += 1
                break
    
    return wordcount


if __name__ == '__main__':
    
    if os.path.exists('./NYT/dataframes/graphing.csv') == True:

        if os.path.exists('./NYT/filtered_data/graphing.json') == True:
        
            occurences = {i: check_occurences(filter[i]) for i in filter}

            with open('./NYT/filtered_data/graphing.json', 'w') as jsonFile:
                json.dump(occurences, jsonFile, indent=4)

        with open('./NYT/filtered_data/graphing.json', 'r') as jsonFile:
            occurences = json.load(jsonFile)

        dfs = {i: pd.json_normalize(occurences[i]).transpose() for i in occurences}

        master_df = pd.DataFrame([])

        for i in dfs:


            dfs[i] = dfs[i].reset_index()
            dfs[i].columns = ['Date', i]
            dfs[i]['Date'] = pd.to_datetime(dfs[i]['Date'])

            try:
                master_df = pd.merge(master_df, dfs[i], on='Date', how='outer')
            except KeyError:
                master_df = dfs[i]
            
            
        master_df = master_df.drop(0, axis='index')
        print(master_df.head())

        master_df.to_csv('./NYT/dataframes/graphing.csv')