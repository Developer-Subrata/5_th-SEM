def bellman(graph,start):
    distances=dict.fromkeys(graph,999)
    distances[start]=0
    pre_nodes=dict.fromkeys(graph,None)
   
    for x in range(len(graph)-1):
        for unvisited in graph:
            for node,weight in graph[unvisited].items():
                if distances[unvisited]+weight<distances[node]:
                    distances[node]=distances[unvisited]+weight
                    pre_nodes[node]=unvisited
    return distances,pre_nodes

graph={}
vertices=int(input("Enter The Number Of Nodes : "))
for i in range(vertices):
    node=input(f"Enter {i+1} Node : ")
    graph[node]={}

edgs=int(input("Enter The Number Of Edges : "))
for i in range(edgs):
    s,e,w=input(f"Enter {i+1} *Start End Weight*=> ").split()
    graph[s][e] = int(w)

print("\nThe Graph Is : \n")
for pn in graph:
    print(f"{pn}: {graph[pn]}")

# Shortest Path Finding
sn=input("Enter Node For Routing Table : ")  #taking input of Starting Node For Routing..

cost,pre_nodes=bellman(graph,sn)

#Printing Routing Table
print(f"\n\tROUTING TABLE FOR '{sn}'")
print("Source\tDestination\tCost\tVia\n")
for nodes in graph:
    via=pre_nodes[nodes] if pre_nodes[nodes] else "_"
    print(f"{sn}\t{nodes}\t\t{cost[nodes]}\t{via}\n")