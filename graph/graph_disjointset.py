def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == "__main__":
    V, E = list(map(int, input().split()))

    parent = [0] * (V + 1)

    for i in range(1, V+1):
        parent[i] = i

    for _ in range(E):
        a, b = list(map(int, input().split()))
        union(parent, a, b)

    print(list(parent))

    for i in range(1, V+1):
        print(find_parent(parent, i))

    for i in range(1, V+1):
        print(f"node: {i}, parent: {parent[i]}")

