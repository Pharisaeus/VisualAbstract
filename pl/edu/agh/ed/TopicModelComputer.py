import logging
from gensim import corpora
from gensim.models import ldamodel
import codecs
import re


def read_stop():
    with codecs.open("stop.txt", "r") as f:
        return set([word.strip() for word in f.read().decode('utf-8').split(',')])


def read_documents(stop_list):
    documents = []
    with codecs.open("pap.txt", "r", 'utf-8') as f:
        data = f.read().lower()
        for document in re.split("#\d+", data):
            normalized_document = []
            for word in re.findall('\w+', document, re.UNICODE):
                if word not in stop_list and word != '':
                    normalized_document.append(word)
            documents.append(" ".join(normalized_document))
    return documents


def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    stop_list = read_stop()
    documents = read_documents(stop_list)[1:]
    texts = [text.split() for text in documents]
    dictionary = corpora.Dictionary.load("e:\\dictionary")
    corpus = [dictionary.doc2bow(text) for text in texts]
    model = ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=100)
    model.save("e:\\lda")

if __name__ == '__main__':
    main()
