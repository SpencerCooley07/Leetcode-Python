from tools import timer
TEST_CASES = [
    "hello",
    "zaz"
]



# TIME: O(n)
# MEM: O(1)
@timer()
def A(s: str) -> int:
    score = 0
    for i in range(1, len(s)): score += abs(ord(s[i-1])-ord(s[i]))
    return score



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(test)
        print()