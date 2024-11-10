# class GraphNode:
#     def __init__(self, val):
#         self.val = val
#         self.neighbors = []

# Or using hashMap method: edges will be given and you have to form adjList dictionary (common)

edges = [['A','B'], ['B','C'], ['B','E'], ['C', 'E'], ['E', 'D']]
adjList = {}
for src, dst in edges:
    if src not in adjList:
        adjList[src] = []
    if dst not in adjList:
        adjList[dst] = []
    adjList[src].append(dst)

def dfs(node, target, adjList, visit):
    if node in visit:
        return 0
    if node == target:
        return 1
    
    count = 0
    visit.add(node)

    for neighbor in adjList[node]:
        count += dfs(neighbor, target, adjList, visit)

    visit.remove(node)
    return count


print(dfs('A', 'E', adjList, set()))
# print(adjList)