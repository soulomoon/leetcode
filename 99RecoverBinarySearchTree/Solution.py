# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return self.val


class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        self.recover(root, 0)

    def recover(self, node, x):
        if node is None:
            return
        node.val = x
        self.recover(node.left, 2 * x + 1)
        self.recover(node.right, 2 * x + 2)

    def find_recursive(self, node, x) -> bool:
        if node is None:
            return False
        elif node.val == x:
            return True
        left = self.find_recursive(node.left, x)
        right = self.find_recursive(node.right, x)
        return left or right

    def find_recursive_fast(self, node, path) -> bool:
        if not path and node:
            return True
        elif not node:
            return False
        elif path.pop():
            return self.find_recursive_fast(node.right, path)
        else:
            return self.find_recursive_fast(node.left, path)

    def find(self, target: int) -> bool:
        path = []
        while target != self.root.val:
            if target % 2 == 0:
                path.append(True)
                target = (target - 2) / 2
            else:
                path.append(False)
                target = (target - 1) / 2
        return self.find_recursive_fast(self.root, path)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
if __name__ == "__main__":
    root = TreeNode(-1)
    root.right = TreeNode(-1)
    finder = FindElements(root)

    print(finder.find(1))
    print(finder.find(2))
