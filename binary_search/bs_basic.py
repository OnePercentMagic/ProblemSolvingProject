def bin_search(arrs, target):
    start = 0
    end = len(arrs) - 1

    while start <= end:
        mid = (start + end) // 2
        if arrs[mid] == target:
            return mid
        elif arrs[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1


if __name__ == "__main__":
    N, target = list(map(int, input().split()))
    arrs = list(map(int, input().split()))
    arrs.sort()
    print(f"arrs: {arrs}")

    res = bin_search(arrs, target)
    print(res)
