import os
os.system('cls')

 
def dfs(graph,v,visited):
    visited[v]=True
    print(v,end='')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

graph = [ [], [2,3,8], [1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visited=[False]*9

dfs(graph,1,visited)


# graph= [[]for _ in range(3)]

# graph[0].append((1,7))
# graph[0].append((2,5))

# graph[1].append((0,7))

# graph[2].append((0,5))

# print(graph)

# if __name__ == __main__:
#     dfs()

