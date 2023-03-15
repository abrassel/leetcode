import indexed_tree

def _permutations(n):
    permutation = [0]*(n+1)
    permutation[0] = 1
    for i in range(1, n+1):
        permutation[i] = i * permutation[i-1]
    return permutation

def _numbers(tree, low, high):
    if low == high:
        return tree
    mid = (high + low) // 2
    tree = tree.insert(mid)
    tree = _numbers(tree, low, mid)
    tree = _numbers(tree, mid + 1, high)
    return tree

def kth_polynomial(n, k):
    permutation = _permutations(n)
    numbers=indexed_tree.singleton_empty_indexed_tree
    numbers = _numbers(numbers, 1, n+1)

    def kth(lst, k):
        if lst.size == 1:
            return f"{lst.value}"
        subset_size = permutation[lst.size-1]
        print(f"subset_size: {subset_size}")
        first_digit_idx = k // subset_size
        print(f"first_digit_idx: {first_digit_idx}")
        first_digit = numbers.get(first_digit_idx)
        print(f"first digit for {k}: {first_digit}")
        return f"{first_digit}{kth(lst.remove(first_digit), k % subset_size)}"

    return kth(numbers, k-1)