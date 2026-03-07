#!/usr/bin/env python
# coding: utf-8

# In[1]:


def dfs(start, goal, graph, visited=None):
    if visited is None:
        visited = set()

    print(start, end=" ")

    if start == goal:
        return True

    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(neighbor, goal, graph, visited):
                return True

    return False


graph = {
    'A':['B','F'],
    'B':['A','C'],
    'C':['B','D'],
    'D':['C','E','H'],
    'E':['A','D'],
    'F':['A','G'],
    'G':['F','H'],
    'H':['G','D']
}

dfs('A','F',graph)


# In[2]:


graph={
    'A':['B','C'],
    'B':['D','E','F'],
    'C':['D','F'],
    'D':['E','F'],
    'E':['F'],
    'F':[]
}
def dfs(graph,node,vis=None):
    if vis is None:
        vis=set()
    if node not in vis:
        print(node,end=" ")
        vis.add(node)
        for neighbor in graph[node]:
            dfs(graph,neighbor,vis)
    return vis
start_node='A'
print("DFS Traversal")
dfs(graph,start_node)


# In[4]:


graph={}
n=int(input("enter no of nodes"))
for i in range(n):
    no=input("enter node name")
    graph[no]=[]
m=int(input("enter no of neighboring node"))
for j in range(m):
    nn=input("enter starting node")
    mm=input("enter ending node")
    graph[nn].append(mm)

    
def dfs(graph, node, vis=None):
    if vis is None:
        vis = set()

    if node not in vis:
        print(node, end=" ")
        vis.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, vis)

    return vis


start = input("\nEnter starting node for DFS: ")

print("DFS Traversal:")
dfs(graph, start)


# In[ ]:




