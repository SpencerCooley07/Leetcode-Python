from tools import timer
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f"[{self.val},{self.left},{self.right}]"

TEST_CASES = [
    TreeNode(10,4,6),
    TreeNode(5,3,1)
]



# TIME: O(1)
# MEM: O(1)
@timer()
def A(root: TreeNode) -> bool:
    return root.val == (root.left + root.right)



if __name__ == "__main__":
    for i, test in enumerate(TEST_CASES):
        print(f'TEST {i+1} - {test}')
        A(test)
        print()