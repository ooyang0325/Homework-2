liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

#use dfs to find the arbitrage path from tokenB to tokenB and print the path and print the balance after the arbitrage
def arbitrage(liquidity, start, end, path, balance):
    if (start == end )& (path != []) & (balance >= 20):
        return path, balance
    for key in liquidity:
        if key[0] == start:
            if key[1] not in path:
                new_balance = liquidity[key][1] - liquidity[key][1] * liquidity[key][0] / (liquidity[key][0] + balance * 0.997)
                new_path = path + [key[1]]
                result = arbitrage(liquidity, key[1], end, new_path, new_balance)
                if result:
                    return result
        elif key[1] == start:
            if key[0] not in path:
                new_balance = liquidity[key][0] - liquidity[key][0] * liquidity[key][1] / (liquidity[key][1] + balance * 0.997)
                new_path = path + [key[0]]
                result = arbitrage(liquidity, key[0], end, new_path, new_balance)
                if result:
                    return result
    return None

path, balance = arbitrage(liquidity, "tokenB", "tokenB", [], 5)
    
print("path: tokenB", end='')
for i in path:
    print("->", i, end='')
    
print(", tokenB balance: ", balance)