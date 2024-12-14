def dijkstra(graph,start):
    distances=dict.fromkeys(graph,999)
    distances[start]=0
    pre_nodes=dict.fromkeys(graph,None)
    unvisited=set(graph)

    while unvisited:
        curr_node=min(unvisited,key=lambda node: distances[node])
        unvisited.remove(curr_node)
        for neighbor,weight in graph[curr_node].items():
            new_distance=distances[curr_node]+weight
            if new_distance<distances[neighbor]:
                distances[neighbor]=new_distance
                pre_nodes[neighbor]=curr_node
    return distances,pre_nodes

graph={}
vertices=int(input("Enter The Number Of Nodes : "))
for i in range(vertices):
    node=input(f"Enter {i+1} Node : ")
    graph[node]={}

edgs=int(input("Enter The Number Of Edges : "))
for i in range(edgs):
    s,e,w=input(f"Enter {i+1} *Start End Weight*=> ").split()
    graph[s][e]=graph[e][s]=int(w)

print("\nThe Graph Is : \n")
for pn in graph:
    print(f"{pn}: {graph[pn]}")

# Shortest Path Finding
sn=input("Enter Node For Routing Table : ")  #taking input of Starting Node For Routing..

cost,pre_nodes=dijkstra(graph,sn)

#Printing Routing Table
print("\n\tROUTING TABLE FOR 'A'")
print("Source\tDestination\tCost\tVia\n")
for nodes in graph:
    via=pre_nodes[nodes] if pre_nodes[nodes] else "_"
    print(f"{sn}\t{nodes}\t\t{cost[nodes]}\t{via}\n")