import codecs
import re
from gensim import corpora
from gensim.models import ldamodel


class TopicModel(object):

    def __init__(self, dictionary, topicsNumber, documentsFile):
        pass
#        self.dictionary = dictionary
#        documents = self.read_documents(dictionary, documentsFile)[1:]
#        all_tokens = sum([document_words for document_words in documents], [])
#        tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
#        texts = [[word for word in document_words if word not in tokens_once] for document_words in documents]
#        self.topicModelDictionary = corpora.Dictionary(texts)
#        corpus = [dictionary.doc2bow(text) for text in texts]
#        self.model = ldamodel.LdaModel(corpus, id2word=self.topicModelDictionary, num_topics=topicsNumber)

    def read_documents(self, dictionary, documentsFile):
        documents = []
        with codecs.open(documentsFile, "r", "utf-8") as f:
            data = f.read().lower()
            for document in re.split("#\d+", data):
                documents.append(dictionary.normalize_document(document))
        return documents

    def print_topics(self, graph):
        pass
#        for color, nodes_list in graph.get_colored_nodes().iteritems():
#            text = [node.get_word() for node in nodes_list]
#            topics_distribution = self.model[self.topicModelDictionary.doc2bow(text)]
#            print color
#            for topic_number, probability in topics_distribution:
#                if probability > 1e-1:
#                    print topic_number, probability
