from tools import timer
TEST_CASES = [
    [7,1,5,4],
    [9,4,3,2],
    [1,5,2,10]
]


# TIME: O(n^2)
# MEM: O(1)
@timer(10)
def A(nums: list[int]) -> int:
    maxDiff = -1
    for i, iNum in enumerate(nums):
        for jNum in nums[(i+1):]:
            if jNum - iNum > maxDiff and iNum != jNum: maxDiff = jNum - iNum
    return maxDiff



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(test)
        print()