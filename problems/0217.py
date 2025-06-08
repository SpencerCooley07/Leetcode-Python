from tools import timer
TEST_CASES = [
    [1,2,3,1],
    [1,2,3,4],
    [1,1,1,3,3,4,3,2,4,2]
]



# TIME: O(n^2)
# MEM: O(1)
@timer()
def A(nums: list[int]) -> bool:
    for i, ie in enumerate(nums):
        for j in range(i+1, len(nums)):
            if ie == nums[j]: return True
    return False

# TIME: O(n)
# MEM: O(n)
@timer()
def B(nums: list[int]) -> bool:
    return len(set(nums)) != len(nums)

# TIME: O(n)
# MEM: O(n)
@timer() # Can be faster in some cases by ending sooner, however B is likely better in most cases
def C(nums: list[int]) -> bool:
    comparison = set()
    for num in nums:
        if num in comparison: return True
        comparison.add(num)
    return False


if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(test)
        B(test)
        C(test)
        print()