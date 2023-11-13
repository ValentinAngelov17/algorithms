def dfs(node, graph, visited):
    if visited[node]:
        return

    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited)


nodes_count = int(input())
edges_count = int(input())

graph = []
[graph.append([]) for _ in range(nodes_count)]

edges = []

for _ in range(edges_count):
    first, second = [int(x) for x in input().split(" - ")]
    graph[first].append(second)
    graph[second].append(first)
    edges.append((min(first, second), max(first, second)))

important_streets = []

for first, second in edges:
    graph[first].remove(second)
    graph[second].remove(first)
    visited = [False] * nodes_count
    dfs(0, graph, visited)

    if not all(visited):
        important_streets.append((first, second))

    graph[first].append(second)
    graph[second].append(first)
print("Important streets:")
for building, street in important_streets:
    print(building, street)

# test input
# 5
# 5
# 1 - 0
# 0 - 2
# 2 - 1
# 0 - 3
# 3 - 4
