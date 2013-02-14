# -*- coding: latin-1 -*-
'''
Created on 7/02/2013
@author: 74187593
'''
from inverted_index import build_inverted_index
from boolean_query import intersect

if __name__ == '__main__':
    my_path = 'C:\\temp\\benedetti'
    document_list = {}
    dictionary = build_inverted_index(my_path, document_list)
    for d in sorted(dictionary.keys()):
        print d + " : " + str(dictionary[d].frequency) + " : " + str(dictionary[d].postings)
    print len(dictionary)
    documents_found = intersect(dictionary[u"alegría"].postings, dictionary["alma"].postings)
    for document_found in documents_found:
        print document_list[document_found]