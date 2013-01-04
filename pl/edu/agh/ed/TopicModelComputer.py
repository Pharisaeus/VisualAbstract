# -*- coding: utf-8 -*-
import logging
from gensim import corpora, models
import os
from gensim.models import ldamodel
import codecs
import re
from Settings import RESOURCES_PATH, STOP_LIST_PATH, WORDS_FORMS_PATH, DICTIONARY_PATH, TFIDF_PATH, LDA_PATH

def read_stop():
    with codecs.open(STOP_LIST_PATH, "r") as f:
        return set([word.strip() for word in f.read().split(',')])


def read_dictionary():
    dictionary = {}
    with codecs.open(WORDS_FORMS_PATH, "r", 'utf-8') as f:
        data = f.read()
        for line in data.split('\n'):
            words = line.split(',')
            for word in words:
                dictionary[word.strip()] = words[0].strip()
    return dictionary


def read_documents(dictionary, stop_list):
    documents = []
    with codecs.open(os.path.join(RESOURCES_PATH, 'pap.txt'), "r", 'utf-8') as f:
        data = f.read().lower()
        for document in re.split("#\d+", data):
            normalized_document = []
            for word in re.findall('\w+', document, re.UNICODE):
                if word not in stop_list and word != '':
                    try:
                        normalized_document.append(dictionary[word])
                    except KeyError:
                        normalized_document.append(word)
                        dictionary[word] = word
            documents.append(normalized_document)
    return documents


def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    dictionary = corpora.Dictionary()
    with codecs.open(os.path.join(RESOURCES_PATH, 'docs'), "r", 'utf-8') as f:
        docs = f.readlines()
        documents = []
        for doc in docs:
            documents.append(doc.split())
        dictionary.add_documents(documents)
        dictionary.save(DICTIONARY_PATH)
        tfidf = models.TfidfModel(dictionary=dictionary)
        tfidf.save(TFIDF_PATH)
        texts = [document for document in documents]
        corpus = [dictionary.doc2bow(text) for text in texts]
        model = ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=50, distributed=False)
        model.save(LDA_PATH)

if __name__ == '__main__':
    main()
