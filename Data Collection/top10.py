

import sys

sys.path.append("./API")


from API import archive


#gets data from a given month
archive = archive.make_url(11, 1961)




 

def word_count(data: list) -> dict: 
    
    #create an empty dictionary
    word_count = {}

    for article in data:

        # go to every article
        for i in range(len(article["keywords"])):

            keyword = article["keywords"][i]["value"]

            # if keyword is in the dictionary, add a point, otherwise, add it to the dictionary
            if keyword in word_count:
                word_count[keyword] += len(article["keywords"]) - i
            else:
                word_count[keyword] = 1

            i += 1


    # for i in word_count:
    #     print(f"{i} - {word_count[i]}")

    return word_count


def top_10(data: list) -> list:
    
    max = 1

    top_10 = []

    for word in data:

        if data[word] > max:
        
            data[word] = max
        
            top_10.append(word)
        
        if len(top_10) > 10:
            top_10 = top_10[1:]

    return top_10


my_list = word_count(archive)

print(top_10(my_list))