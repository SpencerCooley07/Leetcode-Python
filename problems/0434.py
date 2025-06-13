from tools import timer
TEST_CASES = [
    "Hello, my name is John",
    "Hello"
]


# TIME: O(n)
# MEM: O(n)
@timer()
def A(s: str) -> int:
    return len(s.split())



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(test)
        print()