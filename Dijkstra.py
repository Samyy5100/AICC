import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        current_dist, node = heapq.heappop(pq)

        for neighbor, weight in graph[node]:
            distance = current_dist + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return dist

n = int(input("Enter number of nodes: "))

graph = {}

for _ in range(n):
    node = input("Enter node name: ")
    e = int(input(f"Enter number of edges for {node}: "))

    graph[node] = []

    for _ in range(e):
        neighbor = input("Neighbor: ")
        weight = int(input("Weight: "))

        graph[node].append((neighbor, weight))

start = input("Enter start node: ")

print("Shortest Distances:")
print(dijkstra(graph, start))

-----------------Output---------------------
Enter number of nodes: 4

Enter node name: A
Enter number of edges for A: 2
Neighbor: B
Weight: 2
Neighbor: C
Weight: 5

Enter node name: B
Enter number of edges for B: 2
Neighbor: C
Weight: 1
Neighbor: D
Weight: 4

Enter node name: C
Enter number of edges for C: 1
Neighbor: D
Weight: 3

Enter node name: D
Enter number of edges for D: 0

Enter start node: A
