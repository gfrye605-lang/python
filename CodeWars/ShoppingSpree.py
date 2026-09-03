def shopping_spree(p, shop):
    low_to_high = sorted(shop)
    print(low_to_high)
    can_buy = 2
    
    for num in low_to_high:
        print(num)
        if num > p:
            return can_buy
        else:
            num - p
            can_buy =+ 1

