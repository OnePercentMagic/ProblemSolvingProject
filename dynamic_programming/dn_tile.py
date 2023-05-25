def my_func(n):
    if n < 2:
        return 1

    d[1] = 1
    d[2] = 3

    for k in range(3, n+1):
        d[k] = d[k-1] + d[k-2] * 2

    return d[n]


if __name__ == "__main__":
    N = int(input())
    print(f"N: {N}")

    d = [0] * (N+1)

    ans = my_func(N)
    print(ans)
