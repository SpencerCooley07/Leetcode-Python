from tools import timer
TEST_CASES = [
    ([2,7,11,15], 9),
    ([3,2,4], 6),
    ([3,3], 6)
]


# TIME: O(n^2)
# MEM: O(1)
@timer()
def A(nums: list[int], target: int) -> list[int]:
    for i, ie in enumerate(nums[:-1]):
        for j, je in enumerate(nums[(i+1):]):
            if ie + je == target: return [i, j+i+1]

# TIME: O(n^2)
# MEM: O(1)
@timer() # Without list splitting removing per iteration time cost
def B(nums: list[int], target: int) -> list[int]:
    for i, ie in enumerate(nums[:-1]):
        for j in range(i+1, len(nums)):
            if ie + nums[j] == target: return [i, j]

# TIME: O(n)
# MEM: O(n)
@timer()
def C(nums: list[int], target: int) -> list[int]:
    hashMap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashMap: return [hashMap[complement], i]
        hashMap[num] = i
    return nums



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(*test)
        B(*test)
        C(*test)
        print()