def solve(nums, k):
    d = {0:1}
    s = 0
    res = 0
    for x in nums:
        s += x
        res += d.get(s - k, 0)
        d[s] = d.get(s, 0) + 1
    return res

print(solve([1,1,1], 2))
