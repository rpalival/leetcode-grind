# class GraphNode:
#     def __init__(self,val):
#         self.val = val
#         self.neighbors = []

from collections import deque


edges = [['A','B'], ['B','C'], ['B','E'], ['C', 'E'], ['E', 'D']]
adjList = {}
for src, dst in edges:
    if src not in adjList:
        adjList[src] = []
    if dst not in adjList:
        adjList[dst] = []
    adjList[src].append(dst)

def bfs(node, target, adjList):
    length = 0
    visit = set()
    visit.add(node)

    queue = deque()
    queue.append(node)

    while queue:
        for i in range(len(queue)):
            curr = queue.popleft()
            # check if this itself is == target and return
            if curr == target:
                return length
            for neighbor in adjList[curr]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)
        length += 1
    return length

print(bfs('A', 'E', adjList))