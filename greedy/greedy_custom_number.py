
if __name__ == "__main__":
    N, M, K = list(map(int, input().split()))
    arrays = list(map(int, input().split()))
    print(f"N, M, K: {N}, {M}, {K}")
    print(f"arrays: {arrays}")

    # sorts the array
    arrays.sort()
    second, first = arrays[-2:]
    print(f"first: {first}, second: {second}")

    answer = 0
    count = 0

    while count < M:
        if count % K == 0:
            answer += second
        else:
            answer += first
        count += 1
    print(f"answer: {answer}")
