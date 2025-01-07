
[11, 1973]

#start and end is in the form of an array

def get_months(start, end):

    
    list = []

    # sets the year to 1961
    year = start[1]
    month = start[0]


    # stops once it's 1973
    while (end[1] >= year):

        # if it's before 1973
        if end[1] > year:

            #collect every month
            while month <= 12:

                # print(f"{month}/{year}")
                list.append([month, year])

                #change to the next month
                month += 1
            
            #reset to January and go to the next year
            month = 1
            year += 1

        # if it is 1973
        else:
            while month <= end[0]:

                # print(f"{month}/{year}")
                list.append([month, year])

                #change to the next month
                month += 1
        
        # end script
        year += 1

    return list


data = get_months([11, 1961], [8, 1973])

for i in data:
    print(data)