
class Graph:
    def __init__(self, vert_count, graph) -> None:
        self.vert_count = vert_count
        self.graph = graph

    @staticmethod
    def to_full(partial):
        result = {}
        # format v1: [[v2, e1], [v3, e2]] edge between v1 and v2 is e1, and between v1 and v3 is e2
        for v1 in partial:
            if v1 not in result.keys():
                result[v1] = []
            for edge in partial[v1]:
                v2 = edge[0]
                if v2 not in result.keys():
                    result[v2] = []
                result[v1].append([v2, edge[1]])
                result[v2].append([v1, edge[1]])
        return Graph(len(result.keys()), result)

    @staticmethod
    # format [v1, e1, v2] an edge between v1 and v2
    def load_edges(edges):
        result = {}
        for edge in edges:
            if edge[0] not in result.keys():
                result[edge[0]] = []
            if edge[2] not in result.keys():
                result[edge[2]] = []
            result[edge[0]].append([edge[2], edge[1]])
            result[edge[2]].append([edge[0], edge[1]])
        return Graph(len(result.keys()), result)

    def inverse(self):
        result = {}
        print(self.graph)
        for vertex in self.graph:
            for edge in self.graph[vertex]:
                if edge[1] not in result.keys():
                    result[edge[1]] = []
                result[edge[1]].extend([[other, vertex] for other in list(map(lambda e: e[1], self.graph[vertex])) if other != edge[1]])
        return Graph(len(result.keys()), result)

    def reduce(self):
        result = {}
        for vertex in self.graph:
            result[vertex] = list(map(lambda edge: edge[0], self.graph[vertex]))
        return result

    def welsh_powel_cmp(self, v1, v2):
        if len(self.graph[v1]) != len(self.graph[v2]):
            return len(self.graph[v2]) - len(self.graph[v1])
        return -1 if v1 < v2 else 1 if v1 > v2 else 0

    def color(self):
        pass

print(Graph.load_edges([
    ["e1", "a1", "e2"],
    ["e2", "a4", "e3"],
    ["e3", "a3", "e1"],
    ["e3", "a2", "e4"],
]).inverse().graph)
