from tools import timer
TEST_CASES = [
    [1,2],
    [1,2,3,4],
    [-1,1,0,-3,3]
]



# TIME: O(n)
# MEM: O(n)
@timer()
def A(nums: list[int]) -> list[int]:
    lr, rl = [1], [1]
    length = len(nums)
    for f in range(length - 1): lr.append(nums[f] * lr[-1])
    for b in range(length - 1, 0, -1): rl.append(nums[b] * rl[-1])
    return [lr[i] * rl[-i-1] for i in range(length)]


# TIME: O(n)
# MEM: O(1) - Output array in this scenario did not count to space complexity
@timer()
def B(nums: list[int]) -> list[int]:
    n, res = len(nums), [1]
    for f in range(n - 1): res.append(nums[f] * res[-1])
    postfix = 1
    for b in range(n - 1, 0, -1):
        res[b - 1] *= nums[b] * postfix
        postfix *= nums[b]
    return res



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(test)
        B(test)
        print()