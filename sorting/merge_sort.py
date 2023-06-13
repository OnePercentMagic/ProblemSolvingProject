def merge(l1, l2):
    res = []

    while l1 and l2:
        if l1[0] < l2[0]:
            res.append(l1.pop(0))
        else:
            res.append(l2.pop(0))

    if l1:
        res.extend(l1)

    if l2:
        res.extend(l2)

    return res


def merge_v2(l1, l2):
    res = []

    while l1 and l2:
        if l1[0] > l2[0]:
            res.append(l1.pop(0))
        else:
            res.append(l2.pop(0))

    if l1:
        res.extend(l1)

    if l2:
        res.extend(l2)

    return res


def merge_v3(l1, l2):
    res = []
    left = right = 0

    while left < len(l1) and right < len(l2):
        if l1[left] < l2[right]:
            res.append(l1[left])
            left += 1
        else:
            res.append(l2[right])
            right += 1

    res += l1[left:]
    res += l2[right:]

    return res


def merge_sort(nums):
    # base condition
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    l1 = merge_sort(nums[:mid])
    l2 = merge_sort(nums[mid:])

    return merge_v3(l1, l2)


if __name__ == "__main__":
    arrays = list(map(int, input().split()))
    print(f"before sort: {arrays}")

    ans = merge_sort(arrays)

    print(ans)
