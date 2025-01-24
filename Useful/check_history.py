import os

def check_history(main_folder: str):
    #get the last subfolder
    try: 
        year = os.listdir(f'./{main_folder}')[-1]     
    #if no subfolders
    except IndexError:
        print(f'no subfolders in "{main_folder}"')
        return None, None
    
    #get the last file within the subfolder
    try: 
        last_file = os.listdir(f'./{main_folder}/{year}')[-1]
    #if subfolder has no files
    except IndexError:
        print(f'no files in "{main_folder}/{year}"')
        return None, year

    last_filename = last_file.split('.')[0]
    month = last_filename.split('-')[0]
    return month, year


if __name__ == '__main__':

    month, year = check_history('test')
    print(f'Last date entered was "{month}/{year}"')
