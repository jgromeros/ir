'''
Created on 7/02/2013

@author: 74187593
'''
from os import listdir
from fnmatch import fnmatch
import string

def list_files(my_path, extension):
    only_files = [f for f in listdir(my_path) if fnmatch(f, extension)]
    return only_files

def tokenize(my_path, document_name):
    document_words = []
    with open(my_path + '\\' + document_name, 'r') as document:
        for line in document:
            words = line.split(' ')
            words = [''.join(char for char in word if char not in string.punctuation) for word in words]
            document_words.extend([str(word).strip().lower().decode("latin-1") for word in words])
        document_words = [word for word in document_words if word not in string.punctuation]
    return document_words

def build_posting_list(document_words, dictionary, document_index):
    for word in document_words:
        if dictionary.has_key(word):
            try:
                dictionary[word].postings.index(document_index)
            except ValueError:
                dictionary[word].frequency = dictionary[word].frequency + 1
                dictionary[word].postings.append(document_index)
        else:
            posting_list = PostingListItem([])
            posting_list.frequency = 1
            posting_list.postings.append(document_index)
            dictionary[word] = posting_list

def build_inverted_index(corpus_path, document_list):
    dictionary = {}
    document_index = 0
    for document in list_files(corpus_path, '*.txt'):
        document_words = tokenize(corpus_path, document)
        build_posting_list(document_words, dictionary, document_index)
        document_list[document_index] = document
        document_index = document_index + 1
    return dictionary

class PostingListItem:
    '''
    Class to save items from a posting list.
    '''

    '''
    Constructor
    '''
    def __init__(self, postings):
        self.postings = postings
