from tools import timer
TEST_CASES = [
    (4, 1),
    (3, 2)
]



# TIME: O(1)
# MEM: O(1)
@timer()
def A(num: int, t: int) -> int:
    return num + 2 * t



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(*test)
        print()