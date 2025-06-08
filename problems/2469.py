from tools import timer
TEST_CASES = [
    36.50,
    122.11
]



# TIME: O(1)
# MEM: O(1)
@timer()
def A(celsius: float) -> list[float]:
    return [celsius+273.15, celsius*1.8 + 32]



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        print(A(test))
        print()