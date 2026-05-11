import heapq

def prim(graph, start):
    visited = set()
    min_heap = [(0, start)]
    cost = 0

    while min_heap:
        weight, node = heapq.heappop(min_heap)

        if node not in visited:
            visited.add(node)
            cost += weight

            print(node, end=" ")

            for neighbor, w in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (w, neighbor))

    print("\nMinimum Cost =", cost)

n = int(input("Enter number of nodes: "))

graph = {}

for _ in range(n):

    node = input("Enter node: ")
    e = int(input(f"Enter edges for {node}: "))

    graph[node] = []

    for _ in range(e):
        neighbor = input("Neighbor: ")
        weight = int(input("Weight: "))

        graph[node].append((neighbor, weight))

start = input("Enter start node: ")

print("MST Traversal:")
prim(graph, start)


-----------------------Output---------------------
Enter number of nodes: 4

Enter node: A
Enter edges for A: 2
Neighbor: B
Weight: 2
Neighbor: C
Weight: 3

Enter node: B
Enter edges for B: 2
Neighbor: A
Weight: 2
Neighbor: C
Weight: 1

Enter node: C
Enter edges for C: 2
Neighbor: A
Weight: 3
Neighbor: B
Weight: 1

Enter node: D
Enter edges for D: 0

Enter start node: A
