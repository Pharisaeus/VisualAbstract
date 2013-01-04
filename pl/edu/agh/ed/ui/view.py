from flask import render_template
from pl.edu.agh.ed.TextGraphMaker import TextGraphMaker
from pl.edu.agh.ed.ui import app
from flask import request

@app.route('/', methods = ['GET', 'POST'])
def index():
    colored_topic_keywords = {}
    input_text = "Wpisz przykladowy tekst "
    colored_nodes = None
    print request
    if 'text' in request.form and 'percentage' in request.form:
        input_text = request.form['text']
        percentage = int(request.form['percentage'])
        print input_text, percentage
        textGraphMaker = TextGraphMaker()
        graph = textGraphMaker.create_text_graph(input_text, percentage)
        colored_nodes = graph.get_colored_nodes()
        colored_topic_keywords = textGraphMaker.get_topics(graph) # color -> (probability,word)
    return render_template("home.html", text=input_text, colored_nodes=colored_nodes,
        colored_topic_keywords=colored_topic_keywords)



