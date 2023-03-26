def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
    '''
    Return the maximum possible number of integers that may be selected
    while following the following criteria:
        * sum <= maxSum
        * all in [1, n]
        * none in `banned`
        * each chosen integer unique

    The key insight is that it is always better to pick a smaller integer.
    Suppose that the best integer to pick was not the smallest avaiable integer.
    Let's call it p. Then, there is a smaller integer, p-k >= 0.
    If you pick p, then the new sum with which you have to work with is maxSum-p.
    You contribute +1 to the total count.

    On the other hand, if you pick p-k, then your new maxSum is maxSum-p+k which is greater.
    This is your only constraint, and yet you still contributed +1 to the total count.
    Your reward is the same, but the constraint is looser. Therefore, the choice of p was not optimal.
    As a result, you can conclude that a greedy algo of picking the smallest available integer is optimal.
    '''
    banned = set(banned)
    total = 0
    amt = 0
    for i in filter(lambda i: i not in banned, range(1, n+1)):
        total += i
        if total > maxSum:
            break
        amt += 1
    return amt