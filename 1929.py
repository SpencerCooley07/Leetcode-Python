from tools import timer
TEST_CASES = [
    [1,2,1],
    [1,3,2,1]
]



# TIME: O(n)
# MEM: O(n)
@timer
def A(nums: list[int]) -> list[int]:
    return nums + nums



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(test)
        print()