import os

def total_dirlength(root):
    total = 0

    for item in os.listdir(root):
        #if it's a directory, iterate through the directory
        try:
            total += total_dirlength(f'{root}/{item}')
        #if it's a file,
        except NotADirectoryError:
            # print(item)
            total += 1
    
    return total