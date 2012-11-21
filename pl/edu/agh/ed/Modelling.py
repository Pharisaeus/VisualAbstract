# -*- coding: utf-8 -*-
#import collections
#from gensim import corpora
#from gensim.models import ldamodel
#from pl.edu.agh.ed.Graph import Graph
#from pl.edu.agh.ed.community import best_partition
#import networkx as nx
#import logging
#import codecs
#import re
#import pydot


#def draw_text_graph(graph, filename):
#    printable_graph = pydot.Dot(graph_type='graph')
#    for node in graph.get_nodes():
#        printable_node = pydot.Node(node.get_word(), style="filled", fillcolor=node.get_color(), fontsize=node.size() * 10)
#        printable_graph.add_node(printable_node)
#        for neighbour_node in node.get_neighbours():
#            printable_graph.add_edge(pydot.Edge(printable_node, neighbour_node.get_word()))
#    printable_graph.write_png('%s.png' % filename)
#
#
#def main():
#    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)
#    colors = ["red", "green", "blue", "yellow", "pink", "orange", "purple", "white", "violet", "brown", "grey", "red", "green", "blue", "yellow", "pink", "orange", "purple", "white", "violet", "brown", "grey"]
#    normalized_document = read_input("marsz.txt", stop_list, forms_dictionary)
#    graph = create_text_graph(normalized_document, colors)
#    draw_text_graph(graph, "test")
#    print_topics(model, dictionary, graph)
#
#if __name__ == '__main__':
#    main()
