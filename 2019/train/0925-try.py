def sort_csv(file_name, sort_paras: list):
    import pandas as pd
    data = pd.read_csv(file_name)
    data = data.sort_values(sort_paras)
    data.to_csv(file_name, index=False)


def catalan_r(n):
    if n <= 1:
        return 1
    res = 0
    for i in range(n):
        res += catalan_r(i) * catalan_r(n - i - 1)
    return res


# A dynamic programming based function to find nth Catalan number
def catalan_dp(n):
    if n == 0 or n == 1:
        return 1
    # Table to store results of subproblems
    catalan = [0 for i in range(n + 1)]
    # Initialize first two values in table
    catalan[0] = 1
    catalan[1] = 1
    # Fill entries in catalan[] using recursive formula
    for i in range(2, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] = catalan[i] + catalan[j] * catalan[i - j - 1]
    # Return last entry
    return catalan[n]


print(catalan_r(10))
