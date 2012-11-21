# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.utils.datastructures import MultiValueDictKeyError
from django.template.context import RequestContext
from pl.edu.agh.ed.TextGraphMaker import TextGraphMaker


def home(request):
    input_text = "Wpisz przykładowy tekst "
    colored_nodes = None
    try:
        input_text = request.POST['text']
        textGraphMaker = TextGraphMaker()
        graph = textGraphMaker.create_text_graph(input_text)
        colored_nodes = graph.get_colored_nodes()
        textGraphMaker.print_topics(graph)
    except MultiValueDictKeyError:
        print "empty input"
    return render_to_response('home.html', {
                                            'text': input_text,
                                            'colored_nodes': colored_nodes,
                                            },
                              context_instance=RequestContext(request))
