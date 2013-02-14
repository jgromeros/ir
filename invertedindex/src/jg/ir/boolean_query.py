'''
Created on 13/02/2013
@author: 74187593
'''

'''
Method for intersecting the posting lists
'''
from inverted_index import PostingListItem

def intersect(posting_list_1, posting_list_2):
    answer = PostingListItem([])
    for post_1 in posting_list_1:
        for post_2 in posting_list_2:
            if post_1 == post_2:
                answer.postings.append(post_1)
            elif post_1 > post_2:
                continue
            else:
                break
    return answer

def intersect_several(posting_lists):
    import operator
    posting_lists = sorted(posting_lists, key=operator.attrgetter('frequency'))
    if len(posting_lists) <= 1:
        return posting_lists[0]
    else:
        answer = intersect(posting_lists[0].postings, posting_lists[1].postings)
        i = 2
        while i < len(posting_lists):
            answer = intersect(answer.postings, posting_lists[i].postings)
            i +=1
        return answer