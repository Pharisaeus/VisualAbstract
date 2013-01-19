class Node(object):
    def __init__(self, word):
        self.neighbours = []
        self.word = word
        self.color = None
        self.incoming = []
        self.weight = -1

    def connect_to(self, node, edge_weight):
        self.neighbours.append((node, edge_weight))
        node.add_incoming(self)

    def add_incoming(self, node):
        self.incoming.append(node)

    def get_neighbours(self):
        return self.neighbours

    def get_word(self):
        return self.word

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def get_size(self):
        if(self.weight!=-1):
            return self.weight
        return len(self.neighbours) + len(self.incoming)

    def set_weight(self, new_weight):
        self.weight=new_weight
