if __name__ == "__main__":
    N = 1260

    coin_type = [500, 100, 50, 10]
    count = 0

    for coin in coin_type:
        c, N = divmod(N, coin)
        count += c

    print(f"count: {count}")
    assert count == 6, "Wrong answer !"
