
import os
from analyze_data.classes import Article, Folder, File
    

def search(data, y = None, m = None, a = None):


    # if no year specified, pick one
    if y == None:
        year = pick_action(data)
    else:
        year = pick_action(data, y-1960)

    # if no month specified, pick one
    if m == None:
        month = pick_action(year.files)
    else:
        if m < year.files[0].month: m = year.files[0].month
        elif m > year.files[-1].month: m = year.files[-1].month

        month = pick_action(year.files, m)
    
    # generate the data
    month.get_data()

    file_actions = ['Front Page Stats', 'Keyword Stats', 'Article Actions']

    action = pick_action(file_actions)

    if action == file_actions[0]:
        print(f'{month.fpage_frac}')
        print('---------')
        print(f'Percent: {month.fpage_percent}')
        print(f'Ratio: {month.fpage_ratio}')
    elif action == file_actions[1]:
        pass
        #print keywords
    elif action == file_actions[2]:
        #print article actions
        if a == None: article = pick_action(month.fpages)
        else: article = pick_action(month.fpages, a)

        return article


        


def pick_action(action_list, response = None):
    
    if response == None:
        for action in action_list:
            print(f'{action_list.index(action) + 1} - {str(action)}')
        print('----------')
        
        response = int(input('Pick an Action: '))
        while response not in range(len(action_list) + 1):
            response = int(input('Pick an Action: '))
        
        print('===========')

    for action in action_list:
        if action_list.index(action) + 1 == response:
            print(str(action))
            return action
    
    if action == None:
        print(f'{response} not in {action_list}')




folders = os.listdir('./raw_data')

article_data = [Folder(year, 'raw_data') for year in folders]

if __name__ == '__main__':


    article = search(article_data, 1961)
    
    article.rundown()


