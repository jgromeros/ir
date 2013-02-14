'''
Created on 13/02/2013
@author: 74187593
'''

'''
Method for intersecting the posting lists
'''
def intersect(posting_list_1, posting_list_2):
    answer = []
    for post_1 in posting_list_1:
        for post_2 in posting_list_2:
            if post_1 == post_2:
                answer.append(post_1)
            elif post_1 > post_2:
                continue
            else:
                break
    return answer

