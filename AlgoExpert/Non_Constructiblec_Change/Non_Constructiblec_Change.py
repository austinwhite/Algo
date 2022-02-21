# Time: O(nlog(n)) where n=len(coins)
# Space: O(1)

def nonConstructibleChange(coins):
    coins.sort()

    currLargest = 0
    for coin in coins:
        if coin > currLargest + 1:
            break
        else:
            currLargest += coin

    return currLargest + 1
