def quick_sort(arrs):
    if len(arrs) <= 1:
        return arrs

    pivot = arrs[0]
    tail = arrs[1:]

    left_side = [ele for ele in tail if ele < pivot]
    right_side = [ele for ele in tail if ele >= pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


if __name__ == "__main__":
    # quick sort 구현하기
    arrs = list(map(int, input().split()))
    print(f"arrs(before): {arrs}")

    arrs = quick_sort(arrs)
    print(f"arrs(after): {arrs}")
