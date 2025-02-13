try:
    from percent import percent
except ModuleNotFoundError:
    from Useful.percent import percent


def load(i, length, making_newline = False, msg = 'Loading', completion = None):


    if ((type(length) == list) or type(length) == dict) and (type(i) != int) and (i in length): 
        
        try:
            length = list(length.keys())
        except AttributeError:
            pass
        
        i = length.index(i)
        length = len(length)

    if completion == None: completion = msg
    elif completion == True: completion = 'Task Complete!'

    if (i == (length-1)) and making_newline: ending = '\n'
    else: ending = '\r'
    

    if msg == 'progress':

        # get the completion percent
        progress = percent(i, length)


        #state it as an integer percentage
        progress_statement = f'{round(progress, 2)}% Complete'

        #instead of 0 - 99, make it 1 - 100. if it goes over 100 
        if (bar_percent := progress + 1) > 100: bar_percent = 100

        #since the bar is 2 characters, set the length to be integers half the percent
        bar_length = round(bar_percent / 2)


        #if the percent is even, 
        if bar_percent % 2 == 0:
            progress_bar = '[]' * bar_length
        else:
            progress_bar = ('[]' * (bar_length - 1)) + '['

        progress_bar += '_' * (100 - (2 * bar_length))

        
        display = progress_statement + ' \\\\ ' + progress_bar

    else:

        if i != (length-1):
            if i % 4 == 0: dots = ' ' * (3 + len(msg))
            else: dots = '.' * (i % 4)
            display = msg + dots
        else:
            display = f'{' ' * (3 + len(msg))}\r{completion}'
            
        print(display, end=ending)


if __name__ == '__main__':
    for i in range(100):
        load(i, 100)