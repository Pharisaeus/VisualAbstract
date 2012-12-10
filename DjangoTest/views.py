# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.utils.datastructures import MultiValueDictKeyError
from django.template.context import RequestContext
from pl.edu.agh.ed.TextGraphMaker import TextGraphMaker


def home(request):
    colored_topic_keywords = []
    input_text = "Wpisz przykładowy tekst "
    colored_nodes = None
    try:
        input_text = request.POST['text']
        percentage = int(request.POST['percentage'])
        textGraphMaker = TextGraphMaker()
        graph = textGraphMaker.create_text_graph(input_text, percentage)
        colored_nodes = graph.get_colored_nodes()
        colored_topic_keywords = textGraphMaker.get_topics(graph) # color -> (probability,word)
    except MultiValueDictKeyError:
        print "empty input"
    return render_to_response('home.html', {
                                            'text': input_text,
                                            'colored_nodes': colored_nodes,
                                            'colored_topic_keywords': colored_topic_keywords,
                                            },
                              context_instance=RequestContext(request))
