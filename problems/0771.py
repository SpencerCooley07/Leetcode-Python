from tools import timer
from collections import defaultdict
TEST_CASES = [
    ("aA", "aAAbbbb"),
    ("z", "ZZ")
]



# TIME: O(n*m)
# MEM: O(1)
@timer()
def A(jewels: str, stones: str) -> int:
    res = 0
    for jewel in jewels:
        for stone in stones:
            if jewel == stone: res += 1
    return res

# TIME: O(n+m) | n = len(stones) and m = len(jewels)
# MEM: O(n)
@timer() # Better for larger inputs but worse for small inputs
def B(jewels: str, stones: str) -> int:
    res, hashMap = 0, defaultdict(int)
    for stone in stones: hashMap[stone] += 1
    for jewel in jewels: res += hashMap[jewel]
    return res



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(*test)
        B(*test)
        print()