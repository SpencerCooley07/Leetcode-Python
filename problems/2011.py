from tools import timer
TEST_CASES = [
    ["--X","X++","X++"],
    ["++X","++X","X++"],
    ["X++","++X","--X","X--"]
]



# TIME: O(n)
# MEM: O(1)
@timer()
def A(operations: list[str]) -> int:
    x = 0
    for operation in operations:
        if operation[1] == "+": x += 1
        else: x -= 1
    return x



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(test)
        print()