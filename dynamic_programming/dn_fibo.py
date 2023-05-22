def fibo(n):
    d[0] = d[1] = 1

    if d[n] != -1:
        return d[n]

    d[n] = fibo(n-1) + fibo(n-2)

    return d[n]


def fibo_bottom_up(n):
    d[0] = d[1] = 1

    for i in range(2, n+1):
        d[i] = d[i-1] + d[i-2]

    return d[n]


if __name__ == "__main__":
    N = int(input())
    print(f"N: {N}")

    d = [-1] * (N+1)
    # print(fibo(N))

    print(fibo_bottom_up(N))
