def calc_m(arrs, curr):
    ans = 0
    for arr in arrs:
        if arr >= curr:
            ans += arr - curr
        else:
            ans += 0
    return ans


def my_func(arrs, M):
    start = arrs[0]
    end = arrs[-1]

    while start <= end:
        mid = (start + end) // 2

        res = calc_m(arrs, mid)
        if res == M:
            return mid
        elif res > M:
            start = mid + 1
        else:
            end = mid - 1
    return end


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    arrs = list(map(int, input().split()))

    arrs.sort()

    answer = my_func(arrs, M)
    print(f"answer: {answer}")
    print(f"rest: {calc_m(arrs, answer)}")
