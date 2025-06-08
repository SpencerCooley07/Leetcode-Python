from tools import timer
TEST_CASES = [
    [1,2,3,4],
    [1,1,1,1,1],
    [3,1,2,10,1]
]



# TIME: O(n)
# MEM: O(n)
@timer()
def A(nums: list[int]) -> list[int]:
    res, curSum =  [], 0
    for num in nums:
        curSum += num
        res.append(curSum)
    return res

# TIME: O(n)
# MEM: O(1)
# @timer() | Breaks in place solution
def B(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)): nums[i] += nums[i-1]
    print(f"Result: {nums}")
    return nums


if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(test)
        B(test)
        print()