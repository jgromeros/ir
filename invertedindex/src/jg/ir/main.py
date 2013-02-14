# -*- coding: latin-1 -*-
'''
Created on 7/02/2013
@author: 74187593
'''
from inverted_index import build_inverted_index
from boolean_query import intersect_several

if __name__ == '__main__':
    my_path = 'C:\\temp\\benedetti'
    document_list = {}
    dictionary = build_inverted_index(my_path, document_list)
    for d in sorted(dictionary.keys()):
        print d + " : " + str(dictionary[d].frequency) + " : " + str(dictionary[d].postings)
    print len(dictionary)
    answer = intersect_several([dictionary[u"tu"], dictionary[u"por"], dictionary[u"te"]])
    for document_found in answer.postings:
        print document_list[document_found]
    