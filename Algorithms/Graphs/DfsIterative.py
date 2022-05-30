#Dfs iterative

def dfs(graph, source):

    visited = set()
    
    if source not in graph:
        print("Node not in the graph")
        return
    
    stack=[]
    stack.append(source)
    
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for neighbor in graph[current]:
                stack.append(neighbor)




"""
graph={
    
    'A':['B','C','D'], 'B':['E'], 'C':['D','E'], 'D':[], 'E':[]

    }

dfs(graph,'A')
"""
