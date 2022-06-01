#bfs iterative

def bfs(graph, current):
    visited=[]
    queue=[]
    visited.append(current)
    queue.append(current)

    while queue:
        m=queue.pop(0)
        print(m)

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)



"""
graph={
    
    'A':['B','C','D'], 'B':['E'], 'C':['D','E'], 'D':[], 'E':[]

    }


bfs(graph, 'A')
"""