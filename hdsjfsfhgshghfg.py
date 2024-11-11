# Input section
nodes = int(input("Enter the number of nodes: "))
edges_count = int(input("Enter the number of edges: "))
edges = []
node_int = {}  # Dictionary to map node strings to integers for internal processing
node_str = []  # List to map indices back to strings

print("Enter each edge in the format: source destination weight")
for _ in range(edges_count):
    u, v, w = input("Enter source destination weight: ").split()
    w = int(w)

    # Map node names to unique integers
    if u not in node_int:
        node_int[u] = len(node_str)
        node_str.append(u)
    if v not in node_int:
        node_int[v] = len(node_str)
        node_str.append(v)

    # Append mapped edge with integer representations
    edges.append((node_int[u], node_int[v], w))

# Display the edges in a readable format
print(f"{'Source':<10}{'Destination':<15}{'Weight':<10}")
for u, v, w in edges:
    print(f"{node_str[u]:<10}{node_str[v]:<15}{w:<10}")

source_node = input("Enter the source node: ")
source = node_int[source_node]

# Bellman-Ford algorithm implementation
def bellman_ford(nodes, edges, source):
    distance = [float('inf')] * nodes
    previous_nodes = [None] * nodes 
    distance[source] = 0

    # Relax edges
    for _ in range(nodes - 1):
        for u, v, w in edges:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                previous_nodes[v] = u  # Track the path

    # Check for negative-weight cycles
    for u, v, w in edges:
        if distance[u] != float('inf') and distance[u] + w < distance[v]:
            print("Graph contains a negative-weight cycle")
            return None, None

    return distance, previous_nodes

# Run Bellman-Ford and display results
distances, previous_nodes = bellman_ford(nodes, edges, source)
if distances:
    print(f"{'From':<10}{'To':<10}{'Cost':<10}{'Via':<10}")
    for i in range(nodes):
        # Determine the path via previous nodes
        via = node_str[previous_nodes[i]] if previous_nodes[i] is not None else "-"
        print(f"{source_node:<10}{node_str[i]:<10}{distances[i]:<10}{via:<10}")
