import codecs
import re
from Settings import STOP_LIST_PATH, WORDS_FORMS_PATH


class Dictionary(object):
    def __init__(self):
        self.stoplist = self.read_stop()
        self.dictionary = self.read_dictionary()

    def read_stop(self):
        with codecs.open(STOP_LIST_PATH, "r") as f:
            return set([word.strip() for word in f.read().decode('utf-8').split(',')])

    def read_dictionary(self):
        dictionary = {}
        with codecs.open(WORDS_FORMS_PATH, "r", "utf-8") as f:
            data = f.read()
            for line in data.split('\n'):
                words = line.split(',')
                for word in words:
                    dictionary[word.strip()] = words[0].strip()
        return dictionary

    def normalize_document(self, document):
        normalized_document = []
        for word in re.findall('\w+', document.lower(), re.UNICODE):
            if word not in self.stoplist and word != '':
                try:
                    normalized_document.append(self.dictionary[word])
                except KeyError:
                    normalized_document.append(word)
                    self.dictionary[word] = word
        return normalized_document
