#!/usr/bin/env python
# coding: utf-8

# In[2]:


#implemnet of A*
import networkx as nwx
graph=nwx.Graph()
while True:
    choice=int(input("want to insert nodes and edges?press 1 for yes and 2 for no"))
    if choice==1:
        node1=input("enter node").strip().upper()
        node2=input("enter node").strip().upper()
        weight=int(input("enter weight between node1 and node2"))
        graph.add_edge(node1,node2,weight=weight)
    else:
        break
        
graph.adj.items()
for node,neighbor in graph.adj.items():
    print(node,neighbor)
start=input("enter starting node").strip().upper()
goal=input("enter goal node").strip().upper()
graph.nodes()

heuristic_value={}
heuristic_value[goal]=0
for node in graph.nodes():
    if node!=goal:
        heuristic_val=int(input(f"enter heuristic value from node {node} to goal {goal}"))
        heuristic_value[node]=heuristic_val
heuristic_value

def get_heuristic(u,v):
    return heuristic_value[u]
path=nwx.astar_path(graph,start,goal,heuristic=get_heuristic,weight='weight')

total_cost=nwx.astar_path_length(graph,start,goal,heuristic=get_heuristic,weight='weight')
print("optimal path:","->".join(path))
print("totalcost",total_cost)


# In[ ]:




