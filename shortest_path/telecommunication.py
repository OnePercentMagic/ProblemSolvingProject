
N, M, C = list(map(int, input().split()))
print(f"N: {N}, M: {M}, C: {C}")

INF = int(10e9)
# for save the distance
d = [INF] * (N+1)

# for saving adj node
from collections import defaultdict
graph = defaultdict(list)

for _ in range(M):
    X, Y, Z = list(map(int, input().split()))
    graph[X].append((Y, Z))

# start solving problem
from heapq import heappush, heappop

heap = []
d[C] = 0
heappush(heap, (0, C))

while heap:
    dist, now = heappop(heap)

    if d[now] < dist:
        continue

    for nb, time in graph[now]:
        cost = dist + time

        if cost < d[nb]:
            d[nb] = cost
            heappush(heap, (cost, nb))

# count the result
count = 0
max_distance = 0

for i in range(N+1):
    if d[i] != INF and i != C:
        count += 1
        max_distance = max(max_distance, d[i])

print(count, max_distance)






