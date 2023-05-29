
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    # find parent of a
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


if __name__ == "__main__":
    V, E = list(map(int, input().split()))

    parent = [0] * (V+1)

    for i in range(1, V+1):
        parent[i] = i

    cycle = False

    for _ in range(E):
        a, b = list(map(int, input().split()))
        if find_parent(parent, a) == find_parent(parent, b):
            cycle = True
            break
        else:
            union(parent, a, b)

    # cycle
    if cycle:
        print(f"[Cycle] detected!")
    else:
        print(f"No Cycle!")
