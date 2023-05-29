def my_func():
    pass


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    INF = int(10e9)
    graph = [[INF] * (N+1) for _ in range(N+1)]

    for _ in range(M):
        start, end = list(map(int, input().split()))
        graph[start][end] = 1
        graph[end][start] = 1

    X, K = list(map(int, input().split()))

    print(f"N: {N}, M: {M}, X: {X}, K: {K}")

    for k in range(1, N+1):
        for a in range(1, N+1):
            for b in range(1, N+1):
                if a == b:
                    graph[a][b] = 0
                else:
                    graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    ans = graph[1][K] + graph[K][X]
    print(ans)


