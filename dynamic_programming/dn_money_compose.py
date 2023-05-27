def my_func():

    pass


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    print(f"N: {N}, M: {M}")

    arrs = list(map(int, input().split()))
    print(f"arrs: {arrs}")

    d = [10001] * (M+1)

    d[0] = 0

    for i in range(N):
        # arrs[i] 로 만들수 있는 값, di = min(di, di-k + 1)
        for j in range(arrs[i], M+1):
            if d[j-arrs[i]] != 10001:
                d[j] = min(d[j], d[j - arrs[i]] + 1)
    if d[M] ==  10001:
        print(f"No answer ! (-1)")
    else:
        print(d[M])


