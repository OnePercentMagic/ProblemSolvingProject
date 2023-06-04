
if __name__ == "__main__":
    N = int(input())
    arrs = list(map(int, input().split()))

    arrs.sort(reverse=True)
    print(f"N: {N}, arrs: {arrs}")

    count = 0
    while arrs:
        size = arrs[-1]
        if size < len(arrs):
            for _ in range(size):
                arrs.pop()
            count += 1
        else:
            break

    print(f"answer: {count}")
