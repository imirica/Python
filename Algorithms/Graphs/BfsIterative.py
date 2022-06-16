#bfs iterative

def bfs(graph, current):
    visited=[]
    queue=[]
    visited.append(current)
    queue.append(current)

    while queue:
        current=queue.pop(0)
        print(m)

        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)



"""
graph={
    
    'A':['B','C','D'], 'B':['E'], 'C':['D','E'], 'D':[], 'E':[]

    }


bfs(graph, 'A')
"""
"""using set()
def dfs(graph, source):

    visited=set()
    stack=[]
    stack.append(source)

    while stack:
        
        current=stack.pop(0)
        print (current)
        if current not in visited:
            visited.add(current)

        for neighbor in graph[current]:
            stack.append(neighbor)"""
