def binary_search(arrs, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arrs[mid] == target:
            return True
        elif arrs[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return False


def binary_search2(arrs, target, start, end):
    if start > end:
        return False

    mid = (start + end) // 2

    if arrs[mid] == target:
        return True
    elif arrs[mid] > target:
        return binary_search2(arrs, target, start, mid - 1)
    else:
        return binary_search2(arrs, target, mid + 1, end)


if __name__ == "__main__":
    N = int(input())
    total_arrs = list(map(int, input().strip().split()))
    total_arrs.sort()

    M = int(input())
    to_find_arrs = list(map(int, input().strip().split()))
    res = []
    for to_find in to_find_arrs:

        if binary_search2(total_arrs, to_find, 0, len(total_arrs) - 1):
            res.append("yes")
        else:
            res.append("no")

    print(res)
