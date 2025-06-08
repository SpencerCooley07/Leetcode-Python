from tools import timer
from collections import defaultdict
from itertools import chain
TEST_CASES = [
    ([1,1,1,2,2,3], 2),
    ([1,1,1,2,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50], 2),
    ([1], 1)
]



# TIME: O(n+mlog m) | n = len(nums) and m = len(set(nums))
# MEM: O(m)
@timer(100)
def A(nums: list[int], k: int) -> list[int]:
    hashMap = defaultdict(int)
    for num in nums: hashMap[num] += 1
    hashMap = dict(sorted(hashMap.items(), key=lambda x: x[1], reverse=True))
    return list(hashMap.keys())[:k]

# TIME: O(n+m)
# MEM: O(n)
@timer(100) # Theoretically faster, however requires large m (m ≳ 50) due to fast C implementation of sorted()
def B(nums: list[int], k: int) -> list[int]:
    hashMap, frq = defaultdict(int), [[] for _ in range(len(nums))]
    for num in nums: hashMap[num] += 1
    for key, value in hashMap.items(): frq[value-1].append(key)
    return list(chain.from_iterable(frq))[-k:]

# TIME: O(n+m)
# MEM: O(n)
@timer(100) # Avoids flatteng the list, shaving off some time on larger inputs
def C(nums: list[int], k: int) -> list[int]:
    hashMap, frq = defaultdict(int), [[] for _ in range(len(nums))]
    for num in nums: hashMap[num] += 1
    for key, value in hashMap.items(): frq[value-1].append(key)
    res = []
    for i in range(len(frq)-1, -1, -1):
        res.append(frq[i])
        if len(res) == k: return res



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(*test)
        B(*test)
        C(*test)
        print()