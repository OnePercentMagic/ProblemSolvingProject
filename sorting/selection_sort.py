if __name__ == "__main__":
    arrays = list(map(int, input().split()))
    print(f"before sort: {arrays}")

    for i in range(len(arrays)):
        min_idx = i
        for j in range(i+1, len(arrays)):
            if arrays[j] < arrays[min_idx]:
                min_idx = j
        # swap array
        arrays[i], arrays[min_idx] = arrays[min_idx], arrays[i]

    print(f"after sort: {arrays}")
