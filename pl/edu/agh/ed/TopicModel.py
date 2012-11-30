from gensim import corpora, models
from gensim.models import ldamodel


class TopicModel(object):

    def __init__(self, dictionary_path, model_path, tfidf_path):
        self.model = ldamodel.LdaModel.load(model_path)
        self.dictionary = corpora.Dictionary.load(dictionary_path)
        self.tfidf = models.TfidfModel.load(tfidf_path)

    def get_best_matching_topic(self, words):
        relevance = self.model[self.dictionary.doc2bow(words)]
        if len(relevance) > 0:
            sorted_relevance = sorted(relevance, key=lambda tup: tup[1], reverse=True)
            return sorted_relevance[0]
        else:
            return None

    def print_infered_topic(self, color, words):
        relevance = self.model[self.dictionary.doc2bow(words)]
        sorted_relevance = sorted(relevance, key=lambda tup: tup[1], reverse=True)
        print "kolor %s" % color
        for topic, value in sorted_relevance:
            if value > 1e-1:
                print topic, value, words, self.model.show_topic(topic, 10)

    def print_topics(self, graph):
        for color, nodes_list in graph.get_colored_nodes().iteritems():
            text = [node.get_word() for node in nodes_list]
            self.print_infered_topic(color, text)

    def return_top_words(self, word_list, percentage):
        how_many = len(word_list) * (percentage / 100.0)
        words_bow = self.dictionary.doc2bow(word_list)
        keywords = self.tfidf[words_bow]
        best_keywords = []
        sorted_keywords = sorted(keywords, key=lambda tup: tup[1], reverse=True)
        i = 0
        for token_id, _weight in sorted_keywords:
            best_keywords.append(self.dictionary[token_id])
            i += 1
            if i > how_many:
                break
        return set(best_keywords)
