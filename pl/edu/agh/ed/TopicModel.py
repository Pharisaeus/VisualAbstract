from gensim import corpora
from gensim.models import ldamodel


class TopicModel(object):

    def __init__(self, dictionary_path, model_path):
        self.model = ldamodel.LdaModel.load(model_path)
        self.dictionary = corpora.Dictionary.load(dictionary_path)

    def print_infered_topic(self, words):
        relevance = self.model[self.dictionary.doc2bow(words)]
        for topic, value in relevance:
            if value > 1e-1:
                print topic, value

    def print_topics(self, graph):
        for _color, nodes_list in graph.get_colored_nodes().iteritems():
            text = [node.get_word() for node in nodes_list]
            self.print_infered_topic(text)
