def quick_sort(arrs, start, end):
    # inplace version
    if start >= end:
        # no need to sort
        return

    pivot = start

    left = start + 1
    right = end

    while left <= right:

        while left <= end and arrs[left] <= arrs[pivot]:
            left += 1

        while right > start and arrs[right] >= arrs[pivot]:
            right -= 1

        if left > right:  # 엇갈렸으면
            arrs[pivot], arrs[right] = arrs[right], arrs[pivot]
        else:  # 엇갈리지 않은 경우
            arrs[left], arrs[right] = arrs[right], arrs[left]

    quick_sort(arrs, start, right - 1)
    quick_sort(arrs, right + 1, end)


if __name__ == "__main__":
    # quick sort 구현하기
    arrs = list(map(int, input().split()))
    print(f"arrs(before): {arrs}")

    start = 0
    end = len(arrs) - 1

    quick_sort(arrs, start, end)
    print(f"arrs(after): {arrs}")
