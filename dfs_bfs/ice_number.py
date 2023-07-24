

def dfs(r, c):
    if r < 0 or r >=N or c <0 or c >=M:
        return False

    if graph[r][c] == 0:
        graph[r][c] = 1

        # 상, 하 좌 우 모두 체크
        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)

        return True

    return False


if __name__ == "__main__":
    N, M = list(map(int, input().split()))

    graph = []
    for i in range(N):
        graph.append(list(map(int, input())))

    print(graph)

    result = 0

    for r in range(N):
        for c in range(M):
            if dfs(r, c):
                result += 1

    print(result)







