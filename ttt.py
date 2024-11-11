def bellman_ford(graph, start):
    # Initialize distances and previous nodes
    distances = dict.fromkeys(graph, float('inf'))
    distances[start] = 0
    previous_nodes = dict.fromkeys(graph, None)

    # Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    previous_nodes[v] = u

    # Check for negative weight cycles
    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] + weight < distances[v]:
                print("Graph contains a negative weight cycle")
                return None, None

    return distances, previous_nodes

# Initialize graph and input vertices and edges
graph = {}
vertices = int(input("Enter number of vertices: "))

for _ in range(vertices):
    vertex = input("Enter vertex name: ")
    graph[vertex] = {}

edges = int(input("Enter number of edges: "))
for _ in range(edges):
    u, v, w = input("Enter edge (start end weight): ").split()
    graph[u][v] = int(w)  # For a directed graph, remove the bidirectional assignment

print("\nGraph structure:")
for vertex in graph:
    print(f"{vertex}: {graph[vertex]}")

# Input the source node for which to generate the routing table
#sn = input("Enter the vertex for the routing table: ")
# Initialize LST to store routing info for each pair
# LST = []
# nodes = list(graph.keys())  # List of all nodes in the graph

# for sn in nodes:
#     distances, previous_nodes = bellman_ford(graph, sn)

#     if distances:
#         for vertex in nodes:
#             via = previous_nodes[vertex] if previous_nodes[vertex] else "-"
#             LST.append([sn, vertex, distances[vertex], via])

# # Printing the table in the required format
# print("\nRouting Table:")
# # Header row with all destination nodes
# print("      " + "  ".join([f"{node:^7}" for node in nodes]))

# # Fill in each row
# for sn in nodes:
#     row = [f"{sn:^5}"]  # Start row with the source node
#     for vertex in nodes:
#         # Find the cost and via node in LST for this route
#         entry = next((cost_via for src, dst, cost_via, via in LST if src == sn and dst == vertex), None)
#         if entry:
#             cost, via = entry, entry[1]
#             row.append(f"{cost},{via:^3}")
#         else:
#             row.append("N/A")
#     print("  ".join(row))



# Initialize LST to store routing info for each pair
LST = []
nodes = list(graph.keys())  # List of all nodes in the graph

for sn in nodes:
    distances, _ = bellman_ford(graph, sn)  # We're only interested in distances here

    if distances:
        for vertex in nodes:
            cost = distances[vertex] if vertex in distances else "∞"  # Use "∞" if there's no path
            LST.append([sn, vertex, cost])

# Printing the table in the required format
print("\nRouting Table:")
# Header row with all destination nodes
print("      " + "  ".join([f"{node:^5}" for node in nodes]))

# Fill in each row with costs only
for sn in nodes:
    row = [f"{sn:^5}"]  # Start row with the source node
    for vertex in nodes:
        # Find the cost in LST for this route
        entry = next((cost for src, dst, cost in LST if src == sn and dst == vertex), "∞")
        row.append(f"{entry:^5}")
    print("  ".join(row))

