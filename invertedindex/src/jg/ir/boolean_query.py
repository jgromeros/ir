'''
Created on 13/02/2013
@author: 74187593
'''

'''
Method for intersecting the posting lists
'''
from inverted_index import PostingListItem

'''
Function for intersecting two posting lists. This will be done for queries with AND
'''
def intersect(posting_list_1, posting_list_2):
    answer = PostingListItem([])
    i, j = 0, 0
    while nextOrNone(posting_list_1, i) is not None and nextOrNone(posting_list_2, j) is not None:
        if posting_list_1[i] == posting_list_2[j]:
            answer.postings.append(posting_list_1[i])
            i += 1
            j += 1
        elif posting_list_1[i] > posting_list_2[j]:
            j += 1
        else:
            i += 1
    return answer

'''
Function that order posting lists in terms of its frequency. Then intersects the
two posting lists with terms with less frequency, and continues merging posting
lists in increasing order of frequencies
'''
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

'''
Funcion for performing unions between posting lists. Useful when using an OR operator
'''
def union(posting_list_1, posting_list_2):
    answer = PostingListItem([])
    i, j = 0, 0
    while nextOrNone(posting_list_1.postings, i) is not None or nextOrNone(posting_list_2.postings, j) is not None:
        post_1 = nextOrNone(posting_list_1.postings, i)
        post_2 = nextOrNone(posting_list_2.postings, j)
        if post_1 is None:
            answer.postings.append(post_2)
            j += 1
        elif post_2 is None:
            answer.postings.append(post_1)
            i += 1
        elif post_1 == post_2:
            answer.postings.append(post_1)
            i += 1
            j += 1
        elif post_1 > post_2:
            answer.postings.append(post_2)
            j += 1
        else:
            answer.postings.append(post_1)
            i += 1
    return answer

def nextOrNone(posting_list, position):
    try:
        posting = posting_list[position]
    except IndexError:
        posting = None
    return posting