#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import deque
graph={
    'A':['B','C'],
    'B':['D','E','F'],
    'C':['D','F'],
    'D':['E','F'],
    'E':['F'],
    'F':[]
}
def bfs(graph,start):
    vis=set()
    queue=deque([start])
    vis.add(start)
    while queue:
        node=queue.popleft()
        print(node,end=" ")
        for neighbor in graph[node]:
            if neighbor not in vis:
                vis.add(neighbor)
                queue.append(neighbor)
    start_node='A'
    print("BFS Traversal")
    bfs(graph,start_node)


# In[5]:


from collections import deque
graph = {}
n = int(input("enter number of nodes: "))
for i in range(n):
    no = input("enter node name: ")
    graph[no] = []
m = int(input("enter number of neighboring nodes: "))
for i in range(m):
    nn = input("enter starting node: ")
    mm = input("enter ending node: ")
    graph[nn].append(mm)

def bfs(graph, start):
    vis = set()
    queue = deque([start])
    vis.add(start)

    while queue:
        no = queue.popleft()
        print(no, end=" ")

        for neighbor in graph[no]:
            if neighbor not in vis:
                vis.add(neighbor)
                queue.append(neighbor)

start_node = input("enter starting node for BFS: ")
print("BFS Traversal:")
bfs(graph, start_node)


# In[ ]:




