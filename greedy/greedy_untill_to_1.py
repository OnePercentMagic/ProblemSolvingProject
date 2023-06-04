
if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    print(f"N: {N}, M: {M}")

    count = 0
    while N > M:
        while N % M != 0:
            N -= 1
            count += 1

        if N % M == 0:
            N /= M
            count += 1

    # when N < M
    while N > 1:
        count += 1
        N -= 1

    print(f"answer: {count}")
