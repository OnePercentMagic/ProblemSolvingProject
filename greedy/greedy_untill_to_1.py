
if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    print(f"N: {N}, M: {M}")

    count = 0
    if N < M:
        count = N - 1
    else:
        div, res = divmod(N, M)
        count += res
        count += div

    print(f"answer: {count}")
