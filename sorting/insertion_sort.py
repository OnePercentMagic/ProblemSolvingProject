if __name__ == "__main__":
    arrs = list(map(int, input().split()))
    print(f"before: {arrs}")

    # 두번째 항목부터 시작해서 삽입정렬 함
    for i in range(1, len(arrs)):
        for j in range(i, 0, -1):
            if arrs[j] < arrs[j-1]:
                arrs[j], arrs[j-1] = arrs[j-1], arrs[j]
            else:
                break

    print(f"after: {arrs}")
