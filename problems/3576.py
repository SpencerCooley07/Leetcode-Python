from tools import timer
TEST_CASES = [
    ([1,-1,1,-1,1], 3),
    ([-1,-1,-1,1,1,1], 5)
]



# TIME: O(n)
# MEM: O(n)
@timer() # Came up with this in Weekly Contest 453
def A(nums: list[int], k: int) -> bool:
    if abs(sum(nums)) == len(nums): return True

    indexPos = [i for i, num in enumerate(nums) if num == 1]
    indexNeg = [i for i, num in enumerate(nums) if num == -1]

    operations, posLen = 0, len(indexPos)
    if posLen % 2 == 0:
        for i in range(1,len(indexPos),2): operations += (indexPos[i]-indexPos[i-1])
        if operations <= k: return True

    operations, negLen = 0, len(indexNeg)
    if negLen % 2 == 0:
        for i in range(1,len(indexNeg),2): operations += (indexNeg[i]-indexNeg[i-1])
        if operations <= k: return True

    return False



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(*test)
        print()