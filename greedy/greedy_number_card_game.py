import sys

if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    print(f"N: {N}, M: {M}")

    g_max = -sys.maxsize

    # M개의 행을 돌면서 각 행의 최소값 확인하고, global min을 찾기
    for _ in range(N):
        arrs = list(map(int, input().split()))
        arrs.sort()
        local_min = arrs[0]
        if local_min > g_max:
            g_max = local_min

    print(f"answer: {g_max}")
