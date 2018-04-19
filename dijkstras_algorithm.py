# Dijkstras algorithm

graph = {}

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["finish"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["finish"] = 5
graph["finish"] = {}

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 6
costs["finish"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["finish"] = None

processed = []

# to draw graph
import networkx
G = networkx.Graph()
G.add_nodes_from(graph)
G.add_edge("start", "a", weight=6)
G.add_edge("b", "a", weight=3)
G.add_edge("start", "b", weight=2)
G.add_edge("a", "finish", weight=1)
G.add_edge("b", "finish", weight=5)

import matplotlib.pyplot as plt
networkx.draw(G, with_labels=True)
plt.show()
