from tools import timer
TEST_CASES = [
    3,
    5,
    15
]



# TIME: O(n)
# MEM: O(n)
@timer()
def A(n: int) -> list:
    res = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0: res.append("FizzBuzz")
        elif i % 3 == 0: res.append("Fizz")
        elif i % 5 == 0: res.append("Buzz")
        else: res.append(str(i))
    return res



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(test)
        print()