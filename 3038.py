from tools import timer
TEST_CASES = [
    [3,2,1,4,5],
    [1,5,3,3,4,1,3,2,2,3],
    [5,3]
]



# TIME: O(n)
# MEM: O(1)
@timer
def A(nums: list[int]) -> int:
    res, score = 0, nums[0] + nums[1]
    for i in range(1, len(nums), 2):
        if nums[i-1] + nums[i] == score: res += 1
        else: break
    return res



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(test)
        print()