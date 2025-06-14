from tools import timer
TEST_CASES = [
    11891,
    90
]


# TIME: O(n)
# MEM: O(n)
@timer()
def A(num: str) -> int:
    i, num = 0, str(num)
    while i < len(num) and num[i] == "9": i += 1
    if i < len(num):
        return int(num.replace(num[i], '9')) - int(num.replace(num[0], '0'))
    return int(num) - int(num.replace(num[0], '0'))



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(test)
        print()