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
        "STALIN, JOSEPH VISSARIONOVICH",
        'COMMUNIST-WESTERN CONFRONTATION',
        'AMERICAN NATIONS AND WESTERN HEMISPHERE POSSESIONS',
        'AMERICAN NATIONS AND WESTERN HEMISPHERE POSESIONS',
        'AMERICAN NATIONS AND WESTERN HEMISPHERE'


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

        'ARMS CONTROL AND LIMITATION AND DISARMAMENT',
        'ARMS CONTROL AND DISARMAMENT AGENCY',
        'ARMS CONTROL AND DISARMAMENT AGENCY, UNITED STATES',

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

    'Spies and Sabotage': [
        'Espionage',
        'ESPIONAGE AND SUBVERSION',
        'Intelligence',
        'INTERNAL SECURITY',
        'POLITICS AND SECURITY',
        'FOREIGN INTERESTS, AGENTS OF'

    ],

    'Crime and the Police': [
        'POLICE (GENERAL)',
        'Police',
        'POLICE',
        'POLICE DEPATMENT',

        'CRIME',
        'CRIME AND CRIMINAL S',
        'Crime and Criminals',
        'CRIME AND CRIMINALS'
    ]


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