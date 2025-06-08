from tools import timer
TEST_CASES = [
    (12, 5),
    (-10, 4)
]



# TIME: O(1)
# MEM: O(1)
@timer()
def A(num1: int, num2: int) -> int:
    return num1+num2



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(*test)
        print()