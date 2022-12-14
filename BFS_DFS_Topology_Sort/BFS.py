from sys import maxsize
from queue import Queue


class Graph:
    def __init__(self) -> None:
        self.graph = {}

    def addEdge(self, u: int, v: int) -> None:
        if u in self.graph:
            self.graph[u]["adjacent"].append(v)
        else:
            self.graph[u] = {}
            self.graph[u]["property"] = {
                "color": "white",
                "distance": maxsize,
                "parent": None,
            }
            self.graph[u]["adjacent"] = [v]
        if not v in self.graph:
            self.graph[v] = {}
            self.graph[v]["property"] = {
                "color": "white",
                "distance": maxsize,
                "parent": None,
            }
            self.graph[v]["adjacent"] = []

    def printPath(self, s, v):
        if s == v:
            print(v, end=" ")
            return
        elif self.graph[v]["property"]["parent"] == None:
            print(f"No path from {s} to {v}.")
        else:
            self.printPath(s, self.graph[v]["property"]["parent"])
        print(v, end=" ")

    def bfs(self, s: int) -> None:
        # discovering source
        self.graph[s]["property"] = {"color": "gray", "distance": 0, "parent": None}
        # taking a queue
        Q = Queue()
        Q.put(s)

        while not Q.empty():
            u = Q.get()

            # checking all adjacent
            for v in self.graph[u]["adjacent"]:
                if self.graph[v]["property"]["color"] == "white":
                    self.graph[v]["property"] = {
                        "color": "gray",
                        "distance": self.graph[u]["property"]["distance"] + 1,
                        "parent": u,
                    }

                    Q.put(v)

            # finishing u
            self.graph[u]["property"]["color"] = "black"


if __name__ == "__main__":
    g = Graph()
    edge = int(input("Number of Edge: "))
    for i in range(edge):
        u, v = map(int, input("Edge: ").split(" "))
        g.addEdge(u, v)

    source = int(input("Enter the source: "))
    g.bfs(source)
    for key, property in g.graph.items():
        print(key, "-->", property)

    vertex_for_path = int(input("\nEnter the vertex to print path: "))
    g.printPath(source, vertex_for_path)


""" 
input
3
1 2
1 3
2 3
"""


""" 
Number of Edge: 5
Edge: 1 2
Edge: 2 3
Edge: 3 4
Edge: 1 5
Edge: 3 5
Enter the source: 1
1 --> {'property': {'color': 'black', 'distance': 0, 'parent': None}, 'adjacent': [2, 5]}
2 --> {'property': {'color': 'black', 'distance': 1, 'parent': 1}, 'adjacent': [3]}
3 --> {'property': {'color': 'black', 'distance': 2, 'parent': 2}, 'adjacent': [4, 5]}
4 --> {'property': {'color': 'black', 'distance': 3, 'parent': 3}, 'adjacent': []}
5 --> {'property': {'color': 'black', 'distance': 1, 'parent': 1}, 'adjacent': []}

Enter the vertex to print path: 4
1 2 3 4 
"""
