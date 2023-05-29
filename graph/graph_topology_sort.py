
if __name__ == "__main__":
    V, E = map(int, input().split())

    # init indegree
    indegree = [0] * ( V +1)

    import collections
    graph = collections.defaultdict(list)

    # update graph and indegree
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
        indegree[end] += 1

    # queue
    q = collections.deque()

    # add node which has 0 indegree
    for i in range(1, V+ 1):
        if indegree[i] == 0:
            q.append(i)

    res = []

    while q:
        curr = q.popleft()

        # add to result
        res.append(curr)

        # check nb
        for nb in graph[curr]:
            indegree[nb] -= 1

            # add node which has 0 indegree to queue
            if indegree[nb] == 0:
                q.append(nb)

    print(res)
