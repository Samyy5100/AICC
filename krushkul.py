def find(parent, i):
    while parent[i] != i:
        i = parent[i]
    return i

def kruskal(edges, n):

    edges.sort(key=lambda x: x[2])

    parent = [i for i in range(n)]

    cost = 0

    print("Edges in MST:")

    for u, v, w in edges:

        pu = find(parent, u)
        pv = find(parent, v)

        if pu != pv:
            parent[pu] = pv
            cost += w

            print(u, "-", v, "=", w)

    print("Minimum Cost =", cost)

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

for _ in range(e):

    u = int(input("Enter first vertex: "))
    v = int(input("Enter second vertex: "))
    w = int(input("Enter weight: "))

    edges.append((u, v, w))

kruskal(edges, n)

#----------------------OUTPUT----------------------
Enter number of vertices: 4
Enter number of edges: 5
Enter first vertex: 0
Enter second vertex: 1
Enter weight: 10
Enter first vertex: 0
Enter second vertex: 2
Enter weight: 6
Enter first vertex: 0
Enter second vertex: 3
Enter weight: 5
Enter first vertex: 1
Enter second vertex: 3
Enter weight: 15
Enter first vertex: 2
Enter second vertex: 3

Enter weight: 4
Edges in MST: 
0 - 3 = 5
2 - 3 = 4
0 - 1 = 10
Minimum Cost = 19

