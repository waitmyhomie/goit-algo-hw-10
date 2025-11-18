import timeit
from tabulate import tabulate

coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(coins, amount):
    if amount == 0:
        return {}
    
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    
    return result


def find_min_coins(coins, amount):
    if amount == 0:
        return {}
    
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    parent = [-1] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin
    
    if dp[amount] == float('inf'):
        return {}
    
    result = {}
    current = amount
    while current > 0:
        coin = parent[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin
    
    return result


def main():
    # Тестування на різних сумах
    test_amounts = [113, 50, 99, 156, 37]
    
    print("=" * 70)
    print("ТЕСТУВАННЯ НА МАЛИХ СУМАХ")
    print("=" * 70)
    
    for target in test_amounts:
        t1 = timeit.timeit(lambda: find_coins_greedy(coins, target), number=1000)
        t2 = timeit.timeit(lambda: find_min_coins(coins, target), number=1000)
        
        results = [
            ["Greedy", find_coins_greedy(coins, target), f"{t1:.6f} c"],
            ["Dynamic", find_min_coins(coins, target), f"{t2:.6f} c"]
        ]
        
        print(f"\nAmount: {target}")
        print(tabulate(
            results,
            headers=["Algorithm", "Coins", "Time"],
            tablefmt="github"
        ))
    
    # Тестування на великих сумах
    large_amounts = [1000, 5000, 10000, 50000, 100000]
    
    print("\n" + "=" * 70)
    print("ТЕСТУВАННЯ НА ВЕЛИКИХ СУМАХ")
    print("=" * 70)
    
    for target in large_amounts:
        t1 = timeit.timeit(lambda: find_coins_greedy(coins, target), number=100)
        t2 = timeit.timeit(lambda: find_min_coins(coins, target), number=100)
        
        greedy_result = find_coins_greedy(coins, target)
        dp_result = find_min_coins(coins, target)
        
        results = [
            ["Greedy", sum(greedy_result.values()), f"{t1:.6f} c"],
            ["Dynamic", sum(dp_result.values()), f"{t2:.6f} c"]
        ]
        
        print(f"\nAmount: {target}")
        print(tabulate(
            results,
            headers=["Algorithm", "Total Coins", "Time"],
            tablefmt="github"
        ))


if __name__ == "__main__":
    main()