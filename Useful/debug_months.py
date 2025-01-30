from collect_data import archive

if __name__ == '__main__':

    month = int(input('enter a VALID month: '))
    year = int(input('enter a VALID year: '))
    
    archive(int(month), int(year))
    
