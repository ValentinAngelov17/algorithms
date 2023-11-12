def dfs(node, graphs, salaries):
    if salaries[node] is not None:
        return salaries[node]
    if len(graphs[node]) == 0:
        salaries[node] = 1
        return 1
    salary = 0
    for child in graphs[node]:
        salary += dfs(child, graphs, salaries)
    salaries[node] = salary
    return salary


nodes = int(input())
graphs = []

for _ in range(nodes):
    line = input()
    children = []
    for idx, state in enumerate(line):
        if state == 'Y':
            children.append(idx)
    graphs.append(children)

salaries = [None] * nodes
result = 0
for node in range(nodes):
    salary = dfs(node, graphs, salaries)
    result += salary

print(result)
