import random
import networkx as nx
from Settings import DICTIONARY_PATH, LDA_PATH, TFIDF_PATH
from pl.edu.agh.ed.community import best_partition
from pl.edu.agh.ed.TopicModel import TopicModel
from pl.edu.agh.ed.Dictionary import Dictionary
from pl.edu.agh.ed.Graph import Graph


class TextGraphMaker(object):
    __dictionary = Dictionary()
    __topicModel = TopicModel(DICTIONARY_PATH, LDA_PATH, TFIDF_PATH)

    def __init__(self):
        self.dictionary = self.__dictionary
        self.topicModel = self.__topicModel

    def create_text_graph(self, text, percentage, betweenness = True):
        words_list = self.dictionary.normalize_document(text)
        keywords = self.topicModel.return_top_words(words_list, percentage)
        graph = Graph()
        for i in range(len(words_list)):
            if words_list[i] in keywords:
                node = graph.get_node(words_list[i])
                weight = 4
                for next_node_word in words_list[i + 1:i + 4]: #2 nodes ahead
                    if next_node_word in keywords:
                        next_node = graph.get_node(next_node_word)
                        node.connect_to(next_node, weight)
                        weight -= 1
        graph.remove_single_vertices()
        self.color_graph(graph,betweenness)
        return graph

    def color_graph(self, graph,betweenness):
        G = nx.Graph()
        for node in graph.get_nodes():
            G.add_node(node.get_word())
        for node in graph.get_nodes():
            for neighbour_node, _weight in node.get_neighbours():
                G.add_edge(node.get_word(), neighbour_node.get_word())
        groups = best_partition(G)
        communities = self.merge_converging_communities(groups)
        for node in graph.get_nodes():
            node.set_color(communities[node.get_word()])
        if betweenness:
            betweenness_dictionary = nx.betweenness_centrality(G)
            for node in graph.get_nodes():
                node.set_weight(betweenness_dictionary[node.get_word()])

    def merge_converging_communities(self, groups):
        communities = {}
        for color in groups.itervalues():
            communities[color] = [word for word in groups.iterkeys() if groups[word] == color]
        topic_communities = {}
        for color in communities.iterkeys():
            topic, _ = self.topicModel.get_best_matching_topic(communities[color])
            if topic_communities.__contains__(topic) is False:
                topic_communities[topic] = []
            topic_communities[topic].extend(communities[color])
        colored_communities = {}
        for (topic, color) in zip(topic_communities.keys(), communities.keys()):
            for word in topic_communities[topic]:
                colored_communities[word] = color
        return colored_communities

    def print_topics(self, graph):
        self.topicModel.print_topics(graph)

    def get_topics(self, graph):
        sortedTopics = self.topicModel.get_topcis(graph, 40)
        topics = {}
        for color, words in sortedTopics.items():
            randomized = words[:]
            random.shuffle(randomized)
            topics[color] = randomized
        return topics