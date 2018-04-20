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
costs["b"] = 2
costs["finish"] = infinity
print "The weight of each node is: ", costs

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["finish"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
print "Start: the lowest cost node is", node, "with weight",\
    graph["start"]["{}".format(node)]

while node is not None:
    cost = costs[node]
    print "Continue execution ..."
    print "The weight of node {} is".format(node), cost
    neighbors = graph[node]
    if neighbors != {}:
        print "The node {} has neighbors:".format(node), neighbors
    else:
        print "It is finish, we have the answer: {}".format(cost)
    for neighbor in neighbors.keys():
        new_cost = cost + neighbors[neighbor]
        if costs[neighbor] > new_cost:
            costs[neighbor] = new_cost
            parents[neighbor] = node
    processed.append(node)
    print "This nodes we researched:", processed
    node = find_lowest_cost_node(costs)
    if node is not None:
        print "Look at the neighbor:", node

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

print "But the shortest path is:", networkx.shortest_path(G, "start", "finish")

