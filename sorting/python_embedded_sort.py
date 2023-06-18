

if __name__ == "__main__":
    arrs = list(map(int, input().split()))

    print(f"before: {arrs}")
    arrs.sort()
    print(f"after: {arrs}")

    arrs.sort(reverse=True)
    print(f"reverse: {arrs}")