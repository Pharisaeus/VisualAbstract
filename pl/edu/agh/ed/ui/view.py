# coding=utf-8
from flask import render_template
from pl.edu.agh.ed.TextGraphMaker import TextGraphMaker
from pl.edu.agh.ed.ui import app
from flask import request

@app.route('/', methods=['GET', 'POST'])
def index():
    colored_topic_keywords = {}
    colored_nodes = None
    errors = None
    input_text = ""
    if 'text' in request.form and 'percentage' in request.form and 'centrality' in request.form:
        try:
            input_text = request.form['text']
            percentage = float(request.form['percentage'])
            betweenneess = request.form['centrality'] == "betweenness"
            textGraphMaker = TextGraphMaker()
            graph = textGraphMaker.create_text_graph(input_text, percentage, betweenness=betweenneess)
            colored_nodes = graph.get_colored_nodes()
            colored_topic_keywords = textGraphMaker.get_topics(graph) # color -> (probability,word)
        except KeyError:
            errors = "Wprowadzony tekst jest za krotki"
    return render_template("home.html",
        text=input_text,
        colored_nodes=colored_nodes,
        colored_topic_keywords=colored_topic_keywords,
        errors=errors
    )
