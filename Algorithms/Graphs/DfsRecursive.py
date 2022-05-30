visited=set()

def dfs(visited, graph, source):
    if source not in visited:
        print(source)
        visited.add(source)
        for neighbor in graph[source]:
            dfs(visited, graph, neighbor)

"""
graph={
    
    'A':['B','C','D'], 'B':['E'], 'C':['D','E'], 'D':[], 'E':[]

    }

dfs(visited, graph,'A')
"""
