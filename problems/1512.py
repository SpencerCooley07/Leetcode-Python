from tools import timer
from collections import defaultdict
TEST_CASES = [
    [1,2,3,1,1,3],
    [1,1,1,1],
    [1,2,3]
]



# TIME: O(n^2)
# MEM: O(n^2)
@timer()
def A(nums: list[int]) -> int:
    res = 0
    for i in range(len(nums)-1):
        for j, jNum in enumerate(nums[(i+1):]):
            if nums[i] == jNum: res += 1
    return res

# TIME: O(n)
# MEM: O(n)
@timer()
def B(nums: list[int]) -> int:
    count = defaultdict(int)
    res = 0
    for num in nums:
        res += count[num]
        count[num] += 1
    return res


if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(test)
        B(test)
        print()