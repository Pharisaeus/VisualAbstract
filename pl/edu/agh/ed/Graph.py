from pl.edu.agh.ed.Node import Node


class Graph(object):
    def __init__(self):
        self.nodes = {}
        self.known_colors = ['red', '#adff2f', 'green', 'blue', 'orange', 'yellow', 'fuchsia', 'olive', 'purple', 'white', '#87ceeb', '#f0e68c', '#ff8c00', '#228b22', '#ff4500'
        '#4169e1', 'aqua', '#7fff00', '#ff7f50', '#8fbc8f', '#ff6347', 'lime']

    def get_node(self, label):
        if not self.nodes.has_key(label):
            self.nodes[label] = Node(label)
        return self.nodes[label]

    def get_nodes(self):
        return self.nodes.values()

    def get_colored_nodes(self):
        nodes_colors = {}
        for node in self.get_nodes():
                if nodes_colors.has_key(self.get_color_for_id(node.get_color())):
                    nodes_colors[self.get_color_for_id(node.get_color())].append(node)
                else:
                    nodes_colors[self.get_color_for_id(node.get_color())] = [node]
        return nodes_colors

    def get_color_for_id(self, color_id):
        return self.known_colors[color_id % len(self.known_colors)]

    def remove_single_vertices(self):
        connected_vertices = {}
        for label, node in self.nodes.iteritems():
            if node.get_size() > 0:
                connected_vertices[label] = node
        self.nodes = connected_vertices
