def dijkstra(graph, start):
    distances = dict.fromkeys(graph, float('inf'))
    distances[start] = 0
    previous_nodes = dict.fromkeys(graph, None)
    unvisited = set(graph)

    while unvisited:
        current_vertex = min(unvisited, key=lambda v: distances[v])
        unvisited.remove(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            new_distance = distances[current_vertex] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_vertex

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
    graph[u][v] = graph[v][u] = int(w)  # Undirected graph

print("\nGraph structure:")
for vertex in graph:
    print(f"{vertex}: {graph[vertex]}")

# Input the source node for which to generate the routing table
sn = input("Enter the vertex for the routing table: ")

# Apply Dijkstra's algorithm to get distances and paths from the source node
distances, previous_nodes = dijkstra(graph, sn)

# Print the routing table
print(f"\n\tROUTING TABLE FOR *{sn}*\n")
print("From\tTo\tCost\tVia\n")

for vertex in graph:
    via = previous_nodes[vertex] if previous_nodes[vertex] else "-"
    print(f"{sn}\t{vertex}\t{distances[vertex]}\t{via}")