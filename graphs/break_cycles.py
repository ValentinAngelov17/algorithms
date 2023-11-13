def dfs(node, destination, graphs, visited):
    if node in visited:
        return
    visited.add(node)

    if node == destination:
        return

    for child in graphs[node]:
        dfs(child, destination, graphs, visited)


def path_exists(source, destination, graphs):
    visited = set()

    dfs(source, destination, graphs, visited)

    return destination in visited


nodes = int(input())

graphs = {}
edges = []
for _ in range(nodes):
    node, children_str = input().split(" -> ")
    children = children_str.split()
    graphs[node] = children
    for child in children:
        edges.append((node, child))

removed = []
for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
    if destination not in graphs[source] or source not in graphs[destination]:
        continue
    graphs[source].remove(destination)
    graphs[destination].remove(source)

    if path_exists(source, destination, graphs):
        removed.append((source, destination))

    else:
        graphs[source].append(destination)
        graphs[destination].append(source)

print(f'Edges to remove: {len(removed)}')
for key, value in removed:
    print(f"{key} - {value}")


