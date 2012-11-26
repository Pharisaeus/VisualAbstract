import networkx as nx
from pl.edu.agh.ed.community import best_partition
from pl.edu.agh.ed.TopicModel import TopicModel
from pl.edu.agh.ed.Dictionary import Dictionary
from pl.edu.agh.ed.Graph import Graph


class TextGraphMaker(object):

    __dictionary = Dictionary()
    __topicModel = TopicModel(__dictionary, 100, "C:\Users\Pharisaeus\workspace\Python\DjangoTest\static\papsmall.txt")

    def __init__(self):
        self.dictionary = self.__dictionary
        self.topicModel = self.__topicModel

    def create_text_graph(self, text):
        words_list = self.dictionary.normalize_document(text)
        graph = Graph()
        for i in range(len(words_list)):
            node = graph.get_node(words_list[i])
            for next_node_word in words_list[i + 1:i + 4]: #2 nodes ahead
                next_node = graph.get_node(next_node_word)
                node.connect_to(next_node)
        self.color_graph(graph)
        return graph

    def color_graph(self, graph):
        G = nx.Graph()
        for node in graph.get_nodes():
            G.add_node(node.get_word())
        for node in graph.get_nodes():
            for neighbour_node in node.get_neighbours():
                G.add_edge(node.get_word(), neighbour_node.get_word())
        groups = best_partition(G)
        for node in graph.get_nodes():
            node.set_color(groups[node.get_word()])

    def print_topics(self, graph):
        self.topicModel.print_topics(graph)
