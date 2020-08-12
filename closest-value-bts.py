# Average: O(Log(n)) time | O(Log(n)) space
# Worst: O(n) time | O(n) space
# def findClosestValueInBst(tree, target, closest = float("inf")):
#     if tree is None:
#         return closest
#
#     if abs(target - closest) > abs(target - tree.value):
#         closest = tree.value
#
#     if target < tree.value:
#         return findClosestValueInBst(tree.left, target, closest)
#     elif target > tree.value:
#         return findClosestValueInBst(tree.right, target, closest)
#     else:
#         return closest

# Average: O(Log(n)) time | O(1) space
# Worst: O(n) time | O(1) space
def findClosestValueInBst(tree, target, closest = float("inf")):
    currentNode = tree

    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value

        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

tree = Node(10)
tree.left = Node(5)
tree.left.right = Node(5)
tree.left.left = Node(2)
tree.left.left.left = Node(1)
tree.right = Node(15)
tree.right.right = Node(22)
tree.right.left = Node(13)
tree.right.left.left = Node(14)


print(findClosestValueInBst(tree, 12))