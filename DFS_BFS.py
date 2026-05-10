from collections import deque

def bfs(g, start, v):
    visited = [False] * v
    q = deque([start])
    visited[start] = True

    print("BFS:", end=" ")

    while q:
        n = q.popleft()
        print(n, end=" ")

        for i in g[n]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

def dfs(g, node, visited):
    visited[node] = True
    print(node, end=" ")

    for i in g[node]:
        if not visited[i]:
            dfs(g, i, visited)

v = int(input("Number of Vertices: "))
e = int(input("Number of Edges: "))

g = [[] for _ in range(v)]

print("Enter edges connected:")

for _ in range(e):
    u, w = map(int, input().split())
    g[u].append(w)
    g[w].append(u)

start = int(input("Start vertex: "))

bfs(g, start, v)

print("\nDFS:", end=" ")
visited = [False] * v
dfs(g, start, visited)




#----------------------OUTPUT----------------------
# Number of Vertices: 5
# Number of Edges: 4
# Enter edges connected:
# 0 1   
# 0 2
# 1 3       
# 1 4
# Start vertex: 0
# BFS: 0 1 2 3 4
# DFS: 0 1 3 4 2

