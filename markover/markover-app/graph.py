import random

class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent = {}
        self.neighbors = []
        self.weights = []

    def add_edge_to(self, vertex, weight=1):
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + weight

    def generate_probability_mapping(self):
        self.neighbors = list(self.adjacent.keys())
        self.weights = list(self.adjacent.values())

    def get_next_word(self):
        return random.choices(self.neighbors, weights=self.weights)[0]

class Graph:
    def __init__(self):
        self.vertices = {}

    def get_vertex(self, value):
        if value not in self.vertices:
            self.vertices[value] = Vertex(value)
        return self.vertices[value]

    def add_edge(self, from_vertex, to_vertex):
        from_vertex.add_edge_to(to_vertex)

    def generate_probability_mapping(self):
        for vertex in self.vertices.values():
            vertex.generate_probability_mapping()
