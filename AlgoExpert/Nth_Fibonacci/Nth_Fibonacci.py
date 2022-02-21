# Time: O(2^n)
# Space: O(n)

def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getNthFib(n-1) + getNthFib(n-2)

# Time: O(n)
# Space: O(n)

def getNthFib(n):
    memo = {1: 0, 2: 1}
    return getNthFibHelper(n, memo)

def getNthFibHelper(n, memo):
    if n not in memo:
        nth_value = getNthFibHelper(n-1, memo) + getNthFibHelper(n-2, memo)
        memo[n] = nth_value
    return memo[n]
