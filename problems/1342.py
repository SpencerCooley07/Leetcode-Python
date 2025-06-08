from tools import timer
TEST_CASES = [
    14,
    8,
    123
]



# TIME: O(log n)
# MEM: O(1)
@timer()
def A(num: int) -> int:
    count = 0
    while num > 0:
        if num % 2 == 0: num /= 2
        else: num -= 1
        count += 1
    return count



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(test)
        print()