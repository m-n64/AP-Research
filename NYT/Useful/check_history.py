import os

def check_history(main_folder: str):
    #get the last subfolder
    try: 
        year = os.listdir(f'./NYT/{main_folder}')[-1]     
    #if no subfolders
    except IndexError:
        print(f'no subfolders in "{main_folder}"')
        return None, None
    
    #get the last file within the subfolder
    try:


        months = [file.split('-')[0] for file in os.listdir(f'./NYT/{main_folder}/{year}')]
        latest_month = sorted(months, key=lambda file: int(file))[-1]

    #if subfolder has no files
    except IndexError:
        print(f'no files in "{main_folder}/{year}"')
        return None, year

    return latest_month, year


if __name__ == '__main__':

    month, year = check_history('raw_data')
    print(f'Last date entered was "{month}/{year}"')
