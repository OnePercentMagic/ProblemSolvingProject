def my_func(n):

    d[0] = arrays[0]
    d[1] = max(arrays[0], arrays[1])

    for i in range(2, n):
        d[i] = max(d[i-1], d[i-2] + arrays[i])

    return d[n-1]


if __name__ == "__main__":
    N = int(input())
    arrays = list(map(int, input().split()))
    print(f"N: {N}, arrays: {arrays}")

    d = [0] * (N)

    ans = my_func(N)

    print(ans)
