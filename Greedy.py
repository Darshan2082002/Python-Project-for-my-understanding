def greedy_sort(coin,amount):
    coin.sort(reverse=True)
    result=[]
    for c in coin:
        while amount>=c:
            amount-=c
            result.append(c)
    return result
if __name__ == "__main__":
    coins = [1, 5, 10, 25, 30, 63]
    amount = 63
    print("Original coins:", coins)
    print("Amount to make:", amount)
    result = greedy_sort(coins, amount)
    print("Coins used to make change:", result)