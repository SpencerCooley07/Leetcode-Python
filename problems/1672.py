from tools import timer
TEST_CASES = [
    [[1,2,3],[3,2,1]],
    [[1,5],[7,3],[3,5]],
    [[2,8,7],[7,1,3],[1,9,5]]
]



# TIME: O(m*n) | m = len(accounts) and n = len(account)
# MEM: O(1)
@timer()
def A(accounts: list[list[int]]) -> int:
    res = 0
    for account in accounts:
        cur = sum(account)
        if cur > res: res = cur
    return res



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(test)
        print()