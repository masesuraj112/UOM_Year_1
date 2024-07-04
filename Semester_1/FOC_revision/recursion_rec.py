def can_make_change(amount, coins):
    if amount == 0:
        print('I am true')
        return True
    
    if amount < 0 or len(coins) == 0:
        print('I am False')
        return False
    coin = coins[-1]
    print(coins[:-1])
    print(f'{amount} is amount')
    return (can_make_change(amount - coin, coins) or 
            can_make_change(amount, coins[:-1]))
print(can_make_change(23, [3,6,8]))