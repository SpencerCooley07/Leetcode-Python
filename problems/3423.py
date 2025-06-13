from tools import timer
TEST_CASES = [
    [1,2,4],
    [-5,-10,-5]
]



# TIME: O(n)
# MEM: O(1)
@timer()
def A(nums: list[int]) -> int:
    maxDiff = abs(nums[0]-nums[-1])

    for i in range(1, len(nums)):
        diff = abs(nums[i]-nums[i-1])
        if diff > maxDiff: maxDiff = diff

    return maxDiff



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(test)
        print()