from tools import timer
TEST_CASES = [
    "1.1.1.1",
    "255.100.50.0"
]



# TIME: O(n)
# MEM: O(n)
@timer()
def A(address: str) -> str:
    return address.replace(".", "[.]")



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        print(A(test))
        print()