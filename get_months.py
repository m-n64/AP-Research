

#start and end is in the form of an array

def get_months(start_month: int, start_year: int, end_month: int, end_year: int) -> list:

    
    list = []

    # sets the year to 1961
    year = start_year
    month = start_month


    # stops once it's 1973
    while (end_year >= year):

        # if it's before 1973
        if end_year > year:

            #collect every month
            while month <= 12:

                # print(f"{month}/{year}")
                list.append([month, year])

                #change to the next month
                month += 1
            
            #reset to January
            month = 1
        # if it is 1973 (end_year <= 1973)
        else:
            while month <= end_month:

                # print(f"{month}/{year}")
                list.append([month, year])

                #change to the next month
                month += 1
        
        # go to the next year
        year += 1

    return list


if __name__ == "__main__":

    data = get_months(11, 1961, 8, 1973)

    for i in data:
        print(i)