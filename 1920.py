from tools import timer
TEST_CASES = [
    [0,2,1,5,3,4],
    [5,0,1,2,3,4],
    [2,4,0,9,1,8,5,3,6,7]
]



# TIME: O(n)
# MEM: O(n)
@timer()
def A(nums: list[int]) -> list[int]:
    return [nums[num] for num in nums]

# TIME: O(n)
# MEM: O(1)
@timer()
def B(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        nums[i] += 1001 * (nums[nums[i]] % 1001)

    for i in range(len(nums)):
        nums[i] //= 1001
    
    return nums



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(test)
        B(test)
        print()